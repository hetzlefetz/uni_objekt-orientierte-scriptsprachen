from argparse import ArgumentParser
from datetime import datetime
from sys import exit, stderr

from requests import get, head


class Recorder:
    def __init__(
        self, url, file_name="myRadio", duration=30, blocksize=64
    ):
        """
        Constructor for the Recorder class.

        Parameters:
        - url (str): The URL of the audio stream to record.
        - file_name (str, optional): The name of the output file.
        Default is "myRadio".
        - duration (int, optional): The duration of the recording in s.
        Default is 30 seconds.
        - blocksize (int, optional): The block size for data download.
        Default is 64 bytes.
        """
        self.url = url
        self.file_name = file_name
        self.duration = duration
        self.blocksize = blocksize

    def checkUrl(self):
        """
        Check if the provided URL is reachable and valid.

        Returns:
        - bool: True if the URL is reachable and valid, False otherwise.
        """
        code = head(self.url).status_code
        return code in [200, 302, 304]

    def download(self):
        """
        Download the audio stream from the URL and save it to a file.

        The recording will stop after the specified duration.
        """
        if not self.checkUrl():
            print(f"invalid or unreachable url: {self.url}", file=stderr)
            exit(1)

        r = get(self.url, stream=True)
        with open(self.file_name, "wb") as f:
            try:
                start_time = datetime.now()
                for block in r.iter_content(self.blocksize):
                    elapsed_time = datetime.now() - start_time
                    if elapsed_time.total_seconds() >= self.duration:
                        break
                    f.write(block)
                return

            except KeyboardInterrupt:
                exit(-1)


parser = ArgumentParser(
    prog="cli_audiorecorder.py",
    description="A simple command-line MP3 stream recorder utility.",
)
parser.add_argument("url")
parser.add_argument(
    "--filename",
    help="Name of recording",
    default="myRadio",
    nargs="?",
)
parser.add_argument(
    "--duration",
    help="Duration of recording in seconds",
    default="30",
    type=int,
)
parser.add_argument(
    "--blocksize",
    help="Duration of recording in seconds",
    default="64",
    type=int,
)

args = parser.parse_args()

r = Recorder(args.url, args.filename, args.duration, args.blocksize)

r.download()

exit(0)

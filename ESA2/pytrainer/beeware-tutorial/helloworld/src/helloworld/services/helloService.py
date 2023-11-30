class HelloService:
    cnt = 0

    def sayHello(self) -> None:
        print(f"hello {self.cnt}")
        self.cnt += 1

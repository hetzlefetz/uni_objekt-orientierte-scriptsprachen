from kink import di
from helloworld.services.helloService import HelloService

di["hello_service"] = HelloService()

#Instead of directly writing logs everywhere, use an abstract logger:

from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console] {message}")


class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

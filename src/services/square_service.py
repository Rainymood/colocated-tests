from abc import abstractmethod, ABC

class SquareServiceAInterface(ABC):
    @abstractmethod
    def square(self,a):
        raise NotImplementedError


class SquareService(SquareServiceAInterface):
    def __init__(self, name):
        self.name = name

    def square(self, a):
        res = a * a
        print(f"{self.name} :: squaring {a} => {res}")
        return res

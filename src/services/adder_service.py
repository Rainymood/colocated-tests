from abc import abstractmethod, ABC


class AdderServiceInterface(ABC):
    @abstractmethod
    def add(self,a, b):
        raise NotImplementedError


class AdderService(AdderServiceInterface):
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        res = a + b
        print(f"{self.name} :: adding {a} + {b} => {res}")
        return res

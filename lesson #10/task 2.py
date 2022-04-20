from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def calc(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calc(self):
        return 2 * self.size + 0.3


coat = Coat(48)
suit = Suit(4)
print(coat.calc)
print(suit.calc)

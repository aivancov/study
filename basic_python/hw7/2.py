from abc import ABC, abstractmethod

class AbstractClothesClass(ABC):
    @abstractmethod
    def costs(self):
        pass

class Coat(AbstractClothesClass):
    def __init__(self, v):
        self._v = v

    @property
    def costs(self):
        return self._v/6.5 + 0.5


class Suit(AbstractClothesClass):
    def __init__(self, h):
        self._h = h

    @property
    def costs(self):
        return 2*self._h + 0.3



coat = Coat(100)
suit = Suit(100)

print(coat.costs)
print(suit.costs)

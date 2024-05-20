from abc import ABC, abstractmethod


class Thing(ABC):
    hp: int

    @property
    @abstractmethod
    def is_destroyed(self) -> bool:
        return self.hp <= 0


class Tree(Thing):
    hp = 2000

    @property
    def is_destroyed(self):
        return super().is_destroyed


class Rock(Thing):
    hp = 1000

    @property
    def is_destroyed(self):
        return super().is_destroyed

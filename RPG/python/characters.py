from dataclasses import dataclass


@dataclass
class Character:
    hp: int = 1000
    lvl: int = 1

    @property
    def is_alive(self):
        return self.hp > 0

    def attack(self, character: "Character", damage: int):
        character.hp -= damage
        return character.hp

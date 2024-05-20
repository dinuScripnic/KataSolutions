from dataclasses import dataclass, field


@dataclass
class Character:
    hp: int = 1000
    lvl: int = 1
    location: int = 0
    max_range: int = None
    fractions: list[str] = field(default_factory=list)

    @property
    def is_alive(self):
        return self.hp > 0

    def _is_same(self, other: "Character") -> bool:
        return id(self) == id(other)

    def _is_in_range(self, attacked: "Character") -> bool:
        return True

    def _can_attack(self, attacked: "Character") -> bool:
        if not hasattr(attacked, "hp"):
            raise TypeError("Invalid attacked type")
        if self._is_same(attacked):
            raise ValueError("Cannot attack itself")
        if not self._is_in_range(attacked):
            raise ValueError("Character out of range")
        if self.is_allied(attacked):
            raise ValueError("Cannot attack allied character")
        return True

    def _can_heal(self, other: "Character"):
        if not isinstance(other, Character):
            raise TypeError("Invalid character type")
        if not self.is_alive:
            raise ValueError("Dead character cannot be healed")
        if self._is_same(other):
            return True
        if not self.is_allied(other):
            raise ValueError("Cannot heal enemy")
        return True

    def _deal_damage(self, attacked: "Character", damage: int):
        try:
            if self.lvl - attacked.lvl >= 5:
                damage = damage * 1.5
            elif attacked.lvl - self.lvl >= 5:
                damage = damage / 2
        except AttributeError:
            pass

        attacked.hp -= damage

    def attack(self, attacked: "Character", damage: int):
        self._can_attack(attacked)
        self._deal_damage(attacked, damage)

    def heal(self, hp: int, other: "Character" = None):
        if other is None:
            other = self
        self._can_heal(other)
        other.hp = min(1000, other.hp + hp)

    def join_fraction(self, faction: str):
        self.fractions.append(faction)

    def leave_fraction(self, faction: str):
        self.fractions.remove(faction)

    def is_allied(self, other: "Character") -> bool:
        if self.fractions is None or other.fractions is None:
            return False
        # if at least one faction is the same
        # then the characters are alied
        return bool(set(self.fractions) & set(other.fractions))


@dataclass
class MeleeCharacter(Character):
    max_range: int = 2

    def _is_in_range(self, attacked: "Character") -> bool:
        return abs(self.location - attacked.location) <= self.max_range


@dataclass
class RangedCharacter(Character):
    max_range: int = 20

    def _is_in_range(self, attacked: "Character") -> bool:
        return abs(self.location - attacked.location) <= self.max_range

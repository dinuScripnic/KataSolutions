from things import Tree
from characters import Character, MeleeCharacter, RangedCharacter

import pytest


class Test_Character:

    def test_character_defaults_100_hp(self):
        character = Character()
        assert character.hp == 1000

    def test_character_defaults_to_lvl_1(self):
        character = Character()
        assert character.lvl == 1

    def test_character_defaults_to_alive(self):
        character = Character()
        assert character.is_alive is True

    def test_character_can_deal_damage(self):
        character = Character()
        character_attacked = Character()
        character.attack(character_attacked, 10)
        assert character_attacked.hp == 990

    def test_character_can_heal(self):
        character = Character()
        character.hp = 990
        character.heal(10)
        assert character.hp == 1000

    def test_character_can_die(self):
        character = Character()
        character_attacked = Character()
        character.attack(character_attacked, character_attacked.hp)
        assert character_attacked.is_alive is False

    def test_character_dead_cannot_heal(self):
        character = Character()
        character_attacked = Character()
        character.attack(character_attacked, character_attacked.hp)
        with pytest.raises(ValueError):
            character_attacked.heal(10)
        assert character_attacked.hp == 0

    def test_character_cannot_attack_invalid_character(self):
        character = Character()
        with pytest.raises(TypeError):
            character.attack("invalid", 10)

    def test_character_cannot_attack_itself(self):
        character = Character()
        with pytest.raises(ValueError):
            character.attack(character, 10)

    def test_if_attacker_lvl_5_higher_deal_1_5_damage(self):
        character = Character()
        character_attacked = Character()
        character.lvl = 6
        character.attack(character_attacked, 10)
        assert character_attacked.hp == 985

    def test_if_defender_lvl_5_higher_deal_half_damage(self):
        character = Character()
        character_attacked = Character()
        character_attacked.lvl = 6
        character.attack(character_attacked, 10)
        assert character_attacked.hp == 995


class Test_NewCharacters:
    def test_character_has_max_range(self):
        character = Character()
        assert character.max_range is None

    def test_melee_character_has_max_range(self):
        character = MeleeCharacter()
        assert character.max_range == 2

    def test_ranged_character_has_max_range(self):
        character = RangedCharacter()
        assert character.max_range == 20

    def test_character_can_attack_within_range(self):
        character = MeleeCharacter()
        character_attacked = Character()
        character.attack(character_attacked, 10)
        assert character_attacked.hp == 990

    def test_character_cannot_attack_outside_range(self):
        character = MeleeCharacter()
        character_attacked = Character()
        character_attacked.location = 3
        with pytest.raises(ValueError):
            character.attack(character_attacked, 10)

    def test_ranged_character_can_attack_bigger_range(self):
        character = RangedCharacter()
        character_attacked = Character()
        character_attacked.location = 3
        character.attack(character_attacked, 10)
        assert character_attacked.hp == 990

    def test_ranged_character_cannot_attack_outside_range(self):
        character = RangedCharacter()
        character_attacked = Character()
        character_attacked.location = 21
        with pytest.raises(ValueError):
            character.attack(character_attacked, 10)


class Test_Fractions:
    def test_character_can_join_fractions(self):
        character = Character()
        character.join_fraction("fraction")
        assert "fraction" in character.fractions

    def test_character_can_leave_fractions(self):
        character = Character()
        character.join_fraction("fraction")
        character.leave_fraction("fraction")
        assert "fraction" not in character.fractions

    def test_character_can_be_in_multiple_fractions(self):
        character = Character()
        character.join_fraction("fraction1")
        character.join_fraction("fraction2")
        assert "fraction1" in character.fractions
        assert "fraction2" in character.fractions

    def test_character_can_leave_multiple_fractions(self):
        character = Character()
        character.join_fraction("fraction")
        character.join_fraction("fraction2")
        character.leave_fraction("fraction")
        assert "fraction" not in character.fractions
        character.leave_fraction("fraction2")
        assert "fraction2" not in character.fractions

    def test_character_same_fraction_is_allied(self):
        character = Character()
        character2 = Character()
        character.join_fraction("fraction")
        character2.join_fraction("fraction")
        assert character.is_allied(character2)

    def test_characters_are_alies_if_at_least_one_fraction_is_the_same(self):
        character = Character()
        character2 = Character()
        character.join_fraction("fraction")
        character2.join_fraction("fraction2")
        character2.join_fraction("fraction")
        assert character.is_allied(character2)

    def test_character_different_fraction_are_not_allies(self):
        character = Character()
        character2 = Character()
        character.join_fraction("fraction")
        character2.join_fraction("fraction2")
        assert not character.is_allied(character2)

    def test_allies_cannot_attack_each_other(self):
        character = Character()
        character2 = Character()
        character.join_fraction("fraction")
        character2.join_fraction("fraction")
        with pytest.raises(ValueError):
            character.attack(character2, 10)

    def test_allies_can_heal_each_other(self):
        character = Character()
        character2 = Character()
        character.join_fraction("fraction")
        character2.join_fraction("fraction")
        character2.hp = 990
        character.heal(10, character2)
        assert character2.hp == 1000


class Test_Things:
    def test_thing_has_hp(self):
        thing = Tree()
        assert hasattr(thing, "hp")

    def test_thing_is_destroyed(self):
        thing = Tree()
        thing.hp = 0
        assert thing.is_destroyed is True

    def test_thing_can_be_attacked(self):
        thing = Tree()
        character = Character()
        character.attack(thing, 10)
        assert thing.hp == 1990

    def test_thing_can_be_destroyed(self):
        thing = Tree()
        character = Character()
        character.attack(thing, 2000)
        assert thing.is_destroyed is True

    def test_thing_cannot_be_healed(self):
        thing = Tree()
        character = Character()
        with pytest.raises(TypeError):
            character.heal(10, thing)

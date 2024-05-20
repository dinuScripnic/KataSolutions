from characters import Character


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

    def test_character_can_die(self):
        character = Character()
        character_attacked = Character()
        character.attack(character_attacked, character_attacked.hp)
        assert character_attacked.is_alive is False

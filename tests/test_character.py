from game.character.character_logic import Character

def test_exp():
    test_char = Character('Arty')
    actual = test_char.exp_gain(10)
    expected = 10,5
    assert actual == expected

def test_two_levels_exp_gain():
    test_char = Character('Arty')
    actual = test_char.exp_gain(15)
    expected = 15, 0
    assert actual == expected

    actual = test_char.level
    expected = 3

    assert actual == expected

def test_level_up():
    test_char = Character('Arty')
    test_char.level_up()

    actual = test_char.vit
    expected = 12
    assert actual == expected

def test_exp_gain_under_level():
    test_char = Character('Arty')
    actual = test_char.exp_gain(2)
    expected = 5,2
    assert actual == expected

    expected = 1
    assert test_char.level == expected



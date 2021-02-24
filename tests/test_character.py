from game.character.character_logic import Character
from game.merchant.merchant_logic import Items

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

def test_character():
    test_char = Character('Arty')
    actual = test_char.name
    expected = 'Arty'
    assert actual == expected

def test_add_item():
    test_char = Character('Arty')
    test_item = Items('Cain',1,1,1,'sword',20)
    test_char.add_item(test_item)
    actual = test_char.gear['sword']
    expected = test_item
    


def test_pull_stats_sword():
    test_char = Character('Arty')
    test_item = Items('Cain',1,1,1,'sword',20)
    test_char.add_item(test_item)
    test_char.pull_stats()
    actual = test_char.strength
    expected = 9
    assert actual == expected

def test_pull_stats_shield():
    test_char = Character('Arty')
    test_item = Items('Cain',1,1,1,'shield',20)
    test_char.add_item(test_item)
    test_char.pull_stats()
    actual = test_char.strength
    expected = 9
    assert actual == expected

def test_pull_stats_helmet():
    test_char = Character('Arty')
    test_item = Items('Cain',1,1,1,'helmet',20)
    test_char.add_item(test_item)
    test_char.pull_stats()
    actual = test_char.strength
    expected = 9
    assert actual == expected

    
def test_attack_action():
    test_char = Character('Arty')
    actual = test_char.attack()
    expected = 8
    assert actual == expected

    

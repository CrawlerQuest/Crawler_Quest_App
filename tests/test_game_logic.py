import game.game_logic as gm
import mock
import builtins
import unittest
from unittest.mock import patch


def test_load():
    with mock.patch.object(builtins,'input',lambda _:'test_user'):
        test = gm.load()
        actual = test.name
        exp = gm.Character('test_user')
        expected = exp.name
        assert actual == expected

def test_read_file():
    actual = gm.read_file('./tests/test.txt')
    expected = '{im} [a (test)]'
    assert actual == expected

def test_store_story():
    actual = gm.store_story('{im} [a (test)]')
    expected = ("a (test)",)
    assert actual == expected

def test_process_story():
    actual = gm.process_story('{im} [a (test)]\n{me} [as (well)]')
    expected = {'im': ['a (test)'], 'me': ['as (well)']}
    assert actual == expected

def test_get_options():
    test_dict = gm.process_story('{im} [a (test) (me)]\n{me} [as (well)]')
    actual = gm.get_options(test_dict['im'])
    expected = ('test', 'me')
    assert actual == expected

def test_winfight_monster_reset():
    test_char = gm.Character('Arty')
    test_mon = gm.Monster('Siff',1,4,0,7,4)
    test_reset = test_mon.vit
    test_mon.vit = 0
    gm.winfight(test_mon,test_char,test_reset)
    actual = test_mon.vit
    expected = 4
    assert actual == expected

def test_winfight_exp_gain():
    test_char = gm.Character('Arty')
    test_mon = gm.Monster('Siff',1,4,0,7,4)
    test_reset = test_mon.vit
    test_mon.vit = 0
    gm.winfight(test_mon,test_char,test_reset)

    actual = test_char.exp_to_level
    expected = 5
    assert actual == expected

    assert test_char.exp == 4

def test_winfight_potato_gain():
    test_char = gm.Character('Arty')
    test_mon = gm.Monster('Siff',1,4,0,7,4)
    test_reset = test_mon.vit
    test_mon.vit = 0
    gm.winfight(test_mon,test_char,test_reset)
    actual = test_char.potatoes
    expected = 125
    assert actual == expected

def test_take_turn_character_attack():
    with mock.patch.object(builtins,'input',lambda _:'a'):
        test_char = gm.Character('Arty')
        test_mon = gm.Monster('Siff',1,9,0,7,4)

        gm.take_turn(test_char,test_mon)
        actual = test_mon.vit
        expected = 1
        assert actual == expected

def test_take_turn_character_defend():
    with mock.patch.object(builtins,'input',lambda _:'d'):
        test_char = gm.Character('Arty')
        test_mon = gm.Monster('Siff',1,9,0,7,4)

        gm.take_turn(test_char,test_mon)
        actual = test_char.defense
        expected =  3.0
        assert actual == expected

def test_choice_handler_fight():
    with mock.patch.object(builtins,'input',lambda _:'a'):
        test_char = gm.Character('Arty')
        test_char.strength = 99
        test_besti = gm.Bestiary()
        test_story = gm.process_story('{im} [a (test)]\n{me} [as (well)]')
        test_store = gm.Storefront()
        actual = gm.choice_Handler('fight',test_char,test_besti,test_story,0,test_store)
        expected = ('fight',True)
        assert actual == expected

def test_choice_handler_other():
    with mock.patch.object(builtins,'input',lambda _:'a'):
        test_char = gm.Character('Arty')
        test_char.strength = 99
        test_besti = gm.Bestiary()
        test_story = gm.process_story('{im} [a (test)]\n{me} [as (well)]')
        test_store = gm.Storefront()
        actual = gm.choice_Handler('im',test_char,test_besti,test_story,0,test_store)
        expected = (('test',), False)
        assert actual == expected


def test_take_turn_monster():
    test_mon = gm.Monster('Siff',1,1,1,1,1)
    test_char = gm.Character('Arty')
    gm.take_turn(test_mon,test_char)
    actual = test_char.vit
    expected = 8

    assert actual == expected


class Test(unittest.TestCase):
    @patch('builtins.input',side_effect=['armor','plate','z'])
    def test_shop_buy_armor(self,mock_input):
            test_char = gm.Character('Arty')
            test_char.potatoes = 99999
            test_store = gm.Storefront()
            test_item = gm.Items('plate',1,1,1,'helmet',100)
            test_store.armor.append(test_item)
            gm.shop(test_char,test_store)


            actual = test_char.strength
            expected = 9
            assert actual == expected
    
    @patch('builtins.input',side_effect=['weapon','plate','z'])
    def test_shop_buy_weapon(self,mock_input):
            test_char = gm.Character('Arty')
            test_char.potatoes = 99999
            test_store = gm.Storefront()
            test_item = gm.Items('plate',1,1,1,'helmet',100)
            test_store.weapons.append(test_item)
            gm.shop(test_char,test_store)


            actual = test_char.strength
            expected = 9
            assert actual == expected

    @patch('builtins.input',side_effect=['q','e','z','lft','a','quit'])
    def test_play_die_in_dungeon(self,mock_input):
        test_char = gm.Character('Arty')
        test_char.strength = 99
        test_char.exp_to_level = 1
        test_store = gm.Storefront()
        test_besti = gm.Bestiary()
        actual = gm.play(test_char,test_besti,test_store)
        expected = 2
        assert actual == expected





    

    

    




    



    
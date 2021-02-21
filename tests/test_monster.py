from game.monster.monster_logic import Monster, Bestiary

def test_monster_attack():
    test_monst = Monster('John', 10, 11, 12, 13, 2)
    actual = test_monst.attack()[0]
    expected = 10
    assert actual == expected

def test_monster_defend():
    test_monst = Monster('John', 10, 11, 12, 13, 2)
    test_monst.defend()
    actual = test_monst.defense
    expected = 15
    assert actual == expected

def test_monster_haymaker():
    test_monst = Monster('John', 10, 11, 12, 13, 2)
    actual = test_monst.haymaker()[0]
    expected = 12
    assert actual == expected

def test_monster_behavior_above_30():
    test_monst = Monster('John', 10, 11, 12, 13, 2)
    actual = test_monst.behavior()[0]
    expected = 10
    assert actual == expected

# def test_monster_behavior_below_30():
#     test_monst = Monster('John', 10, 11, 12, 13, 2)
#     test_monst.vit - 10
#     actual = test_monst.behavior()[0]
#     expected = 10
#     assert actual == expected

def test_bestiary_randos():
    besti = Bestiary()
    goblin = Monster('gob',2,6,1,4,2)
    imp = Monster('imp',1,6,1,7,2)
    trebble = Monster('TrebbleMaker',3,8,3,4,5 )


    #bigs
    roger = Monster('Rodge',5,20,3,8,20)
    troll = Monster('Troll',4,9,2,5,20)

    besti.randos.append(goblin)
    besti.randos.append(imp)
    besti.randos.append(trebble)

    besti.bosses.append(roger)
    besti.bosses.append(troll)

    actual = besti.randos[0].name
    expected = "gob"
    assert actual == expected

def test_bestiary_bosses():
    besti = Bestiary()
    goblin = Monster('gob',2,6,1,4,2)
    imp = Monster('imp',1,6,1,7,2)
    trebble = Monster('TrebbleMaker',3,8,3,4,5 )


    #bigs
    roger = Monster('Rodge',5,20,3,8,20)
    troll = Monster('Troll',4,9,2,5,20)

    besti.randos.append(goblin)
    besti.randos.append(imp)
    besti.randos.append(trebble)

    besti.bosses.append(roger)
    besti.bosses.append(troll)

    actual = besti.bosses[0].name
    expected = "Rodge"
    assert actual == expected
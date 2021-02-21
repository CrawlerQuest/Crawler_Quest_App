from game.merchant.merchant_logic import Storefront, Items

def test_merchant_storefront_weapon():
    test_merch = Storefront()
    weapon = Items("longsword", 10, 10, 3, "sword", 100)
    shield = Items("shield", 4, 4, 10, "shield", 100)

    test_merch.weapons.append(weapon)

    actual = test_merch.weapons[0].name
    expected = 'longsword'
    assert actual == expected

def test_merchant_storefront_armor():
    test_merch = Storefront()
    weapon = Items("longsword", 10, 10, 3, "sword", 100)
    shield = Items("shield", 4, 4, 10, "shield", 100)

    test_merch.armor.append(shield)

    actual = test_merch.armor[0].name
    expected = 'shield'
    assert actual == expected

# def test_merchant_show_shop():
#     test_merch = Storefront()
#     weapon = Items("longsword", 10, 10, 3, "sword", 100)
#     shield = Items("shield", 4, 4, 10, "shield", 100)

#     test_merch.armor.append(shield)

#     actual = test_merch.show_shop()
#     expected = f"shield\n strength:4\n vitality:4\n defense:10\n cost:100\n "
#     assert actual == expected

def test_merch_items():
    test_items = Items('bow', 10, 11, 12, 'weapon', 100)
   
    actual = test_items.strength
    expected = 10
    assert actual == expected

def test_merch_items_price():
    test_items = Items('bow', 10, 11, 12, 'weapon', 100)
   
    actual = test_items.price
    expected = 100
    assert actual == expected

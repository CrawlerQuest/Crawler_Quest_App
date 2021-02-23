import random

class Storefront:
    def __init__(self):
        self.weapons = []
        self.armor = []

        weapon = Items("longsword", 10, 10, 3, "sword", 100)
        shield = Items("shield", 4, 4, 10, "shield", 100)
        light_sabre = Items("light sabre", 50, 50, 50, "sword", 10000)
        force_field_shield = Items("force field", 4, 4, 10, "shield", 10000)

        self.weapons.append(weapon)
        self.armor.append(shield)
        self.weapons.append(light_sabre)
        self.armor.append(force_field_shield)

    def show_shop(self):
        print("No touch. Buy!")
        wep_display = f"name:"
        for weapon in self.weapons:
            wep_display += f"{weapon.name}\n strength:{weapon.strength}\n vitality:{weapon.vit}\n defense:{weapon.defense}\n cost:{weapon.price}\n\n "
        print(wep_display)
        armor_display = f"armor:"
        for armor in self.armor:
            armor_display += f"{armor.name}\n strength:{armor.strength}\n vitality:{armor.vit}\n defense:{armor.defense}\n cost:{armor.price}\n\n "
        print(armor_display)

    

class Items:
    def __init__(self, name, strength, vit, defense, kind, price):
        self.name = name
        self.strength = strength
        self.vit = vit
        self.defense = defense
        self.price = price
        self.kind = kind

if __name__ == "__main__":
    store = Storefront()
    store.show_shop()



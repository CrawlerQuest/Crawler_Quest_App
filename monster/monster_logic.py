import random
class Monster:
    def __init__(self,name, strength, vitality, defense, malice):
        self.strength = strength
        self.vitality = vitality
        self.defense = defense
        self.malice = malice
        self.id = "m"

    def attack(self):
        return self.strength

    def defend(self):
        self.defense * 1.25

    def haymaker(self):
        return (self.strength + self.malice) - self.vitality

    def behavior(self):
        if self.vitality > (self.vitality * .3):
            return self.attack()
        else:
            chance = random.choice((self.haymaker(), self.defend()))
            return chance
            # does not - char health yet


if __name__ == "__main__":
    monst = Monster("john", 10, 10, 10, 10)
    chance = random.choice((monst.haymaker(), monst.defend()))
    print(chance)
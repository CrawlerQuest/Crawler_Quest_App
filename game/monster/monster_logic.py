import random
class Bestiary:
    def __init__(self):
        self.randos = []
        self.bosses = []
        self.named = []


        #smalls
        goblin = Monster('gob',2,6,1,4)
        imp = Monster('imp',1,6,1,7)
        trebble = Monster('TrebbleMaker',3,8,3,4 )


        #bigs
        roger = Monster('Rodge',5,20,3,8)
        troll = Monster('Troll',4,9,2,5)
        

        self.randos.append(goblin)
        self.randos.append(imp)
        self.randos.append(trebble)

        self.bosses.append(roger)
        self.bosses.append(troll)

    

    
class Monster:
    def __init__(self,name, strength, vit, defense, malice):
        self.strength = strength
        self.name = name
        self.vit = vit
        self.defense = defense
        self.malice = malice
        self.id = "m"

    def attack(self):
        return self.strength

    def defend(self):
        self.defense * 1.25

    def haymaker(self):
        return (self.strength + self.malice) - self.vit

    def behavior(self):
        if self.vit > (self.vit * .3):
            return self.attack()
        else:
            chance = random.choice((self.haymaker(), self.defend()))
            return chance
            # does not - char health yet


if __name__ == "__main__":
    monst = Monster("john", 10, 10, 10, 10)
    chance = random.choice((monst.haymaker(), monst.defend()))
    print(chance)
    besti = Bestiary()
    print(besti.randos)
import random
class Bestiary:
    def __init__(self):
        self.randos = []
        self.bosses = []
        self.named = []


        #smalls
        goblin = Monster('gob',2,6,1,4,2)
        imp = Monster('imp',1,6,1,7,2)
        trebble = Monster('TrebbleMaker',3,8,3,4,5 )


        #bigs
        roger = Monster('Rodge',5,20,3,8,20)
        troll = Monster('Troll',4,9,2,5,20)
        

        self.randos.append(goblin)
        self.randos.append(imp)
        self.randos.append(trebble)

        self.bosses.append(roger)
        self.bosses.append(troll)

    

    
class Monster:
    def __init__(self,name, strength, vit, defense, malice,exp_val):
        self.strength = strength
        self.name = name
        self.vit = vit
        self.defense = defense
        self.malice = malice
        self.id = "m"
        self.exp_val = exp_val
        self.potatoes = 100

    def attack(self):
        return self.strength, 'attack'

    def defend(self):
        self.defense = self.defense * 1.25
        return None, 'defend'

    def haymaker(self):
        return (self.strength + self.malice) - self.vit ,'haymaker'

    def behavior(self):
        if self.vit > (self.vit * .3):
            return self.attack()
        else:
            chance = random.choice((self.haymaker(), self.defend()))
            return chance
            # does not - char health yet
    def scale(self,adv_level):
        self.strength = self.strength + ((self.strength * adv_level)*.85) 
        self.vit = self.vit + ((self.strength * adv_level)*.75)
        self.defense = self.defense + ((self.defense * adv_level)*.75)
        self.exp_val = (self.exp_val * adv_level) * .90
        self.potatoes = 100 * adv_level







class Character:
    def __init__(self,name):
        self.strength = 5
        self.vit = 5
        self.defense = 1
        self.gear = []
        self.name = name
        self.id = "c"


    def sword(self,name,strength,vit):
        self.strength += strength
        self.vit += vit
        self.gear.append(name)

    def shield(self,name,strength,vit, defense):
        self.strength += strength
        self.vit += vit
        self.defense += defense
        self.gear.append(name)

    def helmet(self,name,strength,vit, defense):
        self.strength += strength
        self.vit += vit
        self.defense += defense
        self.gear.append(name)

    def attack(self):
        return self.strength

    def defend(self):
        self.defense = self.defense * 1.25

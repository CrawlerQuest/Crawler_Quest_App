class Character:
    def __init__(self,name):
        self.strength = 8
        self.vit = 9
        self.defense = 2
        self.gear = {
        "sword": None,
        "shield": None,
        "helmet": None}
        self.name = name
        self.id = "c"
        self.level = 1
        self.exp = 0 
        self.exp_to_level = 5
        self.potatoes = 25

    def add_item(self, item):
        self.gear[item.kind] = item

    def pull_stats(self):
        if self.gear["sword"]:
            self.strength += self.gear["sword"].strength
            self.vit += self.gear["sword"].vit
            self.defense += self.gear["sword"].defense
        if self.gear["helmet"]:
            self.strength += self.gear["helmet"].strength
            self.vit += self.gear["helmet"].vit
            self.defense += self.gear["helmet"].defense
        if self.gear["shield"]:
            self.strength += self.gear["shield"].strength
            self.vit += self.gear["shield"].vit
            self.defense += self.gear["shield"].defense

                
    def attack(self):
        return self.strength

    def defend(self):
        self.defense = self.defense * 1.50

    def take_pots(self, potatoe):
        self.potatoes += potatoe
    
    def exp_gain(self,exp_gain):
        """[takes in int of experience and subtracts from needed exp to level]
        Calls:
            level up
        """
        self.exp += exp_gain
        while self.exp >= self.exp_to_level:
            self.exp -= self.exp_to_level
            self.level_up()
        
        return self.exp_to_level,self.exp


    def level_up(self):
        """[used to level up character]
        """
        self.level += 1
        self.strength +=2
        self.vit += 3
        self.defense +=1
        self.exp_to_level = self.level * 5
        print(f"""
        You leveled UP!
        Level:{self.level}
        Strength:{self.strength}
        Vitality:{self.vit}
        Defence:{self.defense}""")




        
            




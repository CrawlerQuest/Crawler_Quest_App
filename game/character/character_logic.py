class Character:
    def __init__(self,name):
        self.strength = 8
        self.vit = 9
        self.defense = 4
        self.gear = []
        self.name = name
        self.id = "c"
        self.level = 1
        self.exp_to_level = 5


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
        self.defense = self.defense * 1.50
    
    def exp_gain(self,exp):
        """[takes in int of experience and subtracts from needed exp to level]
        Calls:
            level up
        """
        exp_calc = self.exp_to_level - exp
        if exp_calc > 0:
            self.exp_to_level = exp_calc
        while exp_calc <= 0:
            self.level_up()
            exp_calc += self.exp_to_level
            self.exp_to_level -= exp_calc
        return self.exp_to_level
        

    def level_up(self):
        """[used to level up character]
        """
        self.level += 1
        self.strength +=2
        self.vit += 3
        self.defense +=1
        self.exp_to_level += self.exp_to_level
        print(f"""
        You leveled UP!
        Level:{self.level}
        Strength:{self.strength}
        Vitality:{self.vit}
        Defence:{self.defense}""")
        
            




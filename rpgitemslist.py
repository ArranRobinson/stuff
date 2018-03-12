class Item:
    def __init__(self, name1, cost1, atk1, def1, spd1):
        self.name = name1
        self.cost = cost1
        self.atk = atk1
        self.defense = def1
        self.spd = spd1

        
#List of Items

class Potion(Item):

    hpgain = 0
    mpgain = 0
    

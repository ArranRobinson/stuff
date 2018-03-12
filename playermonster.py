import random

BlankMatrix = []

class Entity:
    def __init__(self, hp1, atk1, def1, spd1, matk1, mdef1, luk1, mp1):
        self.maxHp = hp1
        self.curHP = hp1
        self.maxAtk = atk1
        self.maxDefense = def1
        self.maxSpeed = spd1
        self.maxMatk = matk1
        self.maxMdef = mdef1
        self.maxLuk = luk1
        self.maxMP = mp1
        isDead = False
    def hpChange(amountChange, direct):
        curHP = curHP-(amountChange*direct)
        if (curHP > maxHp):
            curHP = maxHp
        if (curHP <= 0):
            isDead = True
    def checkDeath(dead):
        if (dead == True):
            del self

class Specialty:
    def __init__(self, name1, hpbonus1, atkbonus1, defbonus1, spdbonus1, matkbonus1, mdefbonus1, lukbonus1, mpbonus1, inctable1):
        self.name = name1
        self.hpbonus = hpbonus1
        self.atkbonus = atkbonus1
        self.defbonus = defbonus1
        self.spdbonus = spdbonus1
        self.matkbonus = matkbonus1
        self.mdefbonus = mdefbonus1
        self.lukbonus = lukbonus1
        self.inctable = inctable1
        self.mpbonus = mpbonus1
        


#Player Class

class Player(Entity):
    exp = 0
    h = 10
    w = 2
    Inventory = [[0 for x in range(2)] for y in range(h)]
    name = ""
    level = 1
    PlayerSpecialty = Specialty("", 0, 0, 0, 0, 0, 0, 0, 0, BlankMatrix)
    gold = 0

    def UpdateStats(self):
        self.maxHp = self.maxHp + self.PlayerSpecialty.hpbonus
        self.maxAtk = self.maxAtk + self.PlayerSpecialty.atkbonus
        self.maxDefense = self.maxDefense + self.PlayerSpecialty.defbonus
        self.maxSpeed = self.maxSpeed + self.PlayerSpecialty.spdbonus
        self.maxMatk = self.maxMatk + self.PlayerSpecialty.matkbonus
        self.maxMdef = self.maxMdef + self.PlayerSpecialty.mdefbonus
        self.maxLuk = self.maxLuk + self.PlayerSpecialty.lukbonus
        self.maxMP = self.maxMP + self.PlayerSpecialty.mpbonus

    def SetSpecialty(self, name1, xptable, PlayerSpecialty):
        PlayerSpecialty.name = name1
        PlayerSpecialty.inctable = xptable
        PlayerSpecialty.hpbonus = xptable[2][0]
        PlayerSpecialty.atkbonus = xptable[3][0]
        PlayerSpecialty.defbonus = xptable[4][0]
        PlayerSpecialty.spdbonus = xptable[5][0]
        PlayerSpecialty.matkbonus = xptable[6][0]
        PlayerSpecialty.mdefbonus = xptable[7][0]
        PlayerSpecialty.lukbonus = xptable[8][0]
        PlayerSpecialty.mpbonus = xptable[9][0]
        self.UpdateStats()
    
    def PrintStats(self):
        print("NAME: " + self.name)
        print("SPECIALTY: " + self.PlayerSpecialty.name)
        print("HP: " + str(self.maxHp))
        print("MP " + str(self.maxMP))
        print("ATK: " + str(self.maxAtk))
        print("DEF: " + str(self.maxDefense))
        print("SPD: " + str(self.maxSpeed))
        print("MATK: " + str(self.maxMatk))
        print("MDEF: " + str(self.maxMdef))
        print("LUK: " + str(self.maxLuk))

    def AddGold(self, amount):
        self.gold += amount

    def RemoveGold(self, amount):
        self.gold -= amount

    def LevelUp(self):
        while True:
            if (self.exp >= self.PlayerSpecialty.inctable[1][level]):
                level += 1
    
        

    #def addItem(item)
    #    i = 0
    #    while(i <= h):
    #        if(item == inventory[i]):
    #            Inventory[i][1]++

#Player Creation

h1 = 10
w1 = 10

#healerxpTable
HealerXPTable = [[0 for x in range(w1)] for y in range(h1)]
#level1
HealerXPTable[0][0] = 1
HealerXPTable[1][0] = 0
HealerXPTable[2][0] = 5
HealerXPTable[3][0] = 1
HealerXPTable[4][0] = 2
HealerXPTable[5][0] = 2
HealerXPTable[6][0] = 1
HealerXPTable[7][0] = 3
HealerXPTable[8][0] = 1
HealerXPTable[9][0] = 4

#level2
HealerXPTable[0][1] = 2
HealerXPTable[1][1] = 100
HealerXPTable[2][1] = 10
HealerXPTable[3][1] = 4
HealerXPTable[4][1] = 5
HealerXPTable[5][1] = 5
HealerXPTable[6][1] = 4
HealerXPTable[7][1] = 7
HealerXPTable[8][1] = 4
HealerXPTable[9][1] = 8



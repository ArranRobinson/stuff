#RPG Game

import random
import rpgitemslist
import playermonster



def DiceRoller(beginNum, endNum):
    num = random.randint(beginNum, endNum)
    print(num)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#BaseClasses

at = random.randint(3, 10)
de = random.randint(3, 10)
sp = random.randint(3, 10)
mat = random.randint(3, 10)
mde = random.randint(3, 10)
lu = random.randint(3, 10)

specialtyList = ["Healer", "Warrior", "Mage", "Trainer", "Dancer", "Thief"]

selectedSpecialty = 0

ans1 = ""

p = playermonster.Player(100, at, de, sp, mat, mde, lu, 50)

while True:
    print ("Please enter your name")

    named = input()

    p.name = named

    if (ans1 != 'Y' or ans1 != 'N'):
        print (p.name + ", right? (Enter Y for yes or N for no)")

        ans1 = str(input())
        ans1 = ans1.upper()

    if (ans1 =='Y'):
        break



print("Select your Specialty!")

n = 1
for i in specialtyList:
    print("[" + str(n) + "] " + i)
    n = n+1

while True: 
    specialtyChoice = input()

    if (is_number(specialtyChoice) == False):
        print("Please enter a valid numerical value")
              
    if (int(specialtyChoice) == 1):
        p.SetSpecialty(specialtyList[int(specialtyChoice)-1], playermonster.HealerXPTable, p.PlayerSpecialty)
        break


print( "Welcome " + p.name + ", the " + p.PlayerSpecialty.name)

p.PrintStats()

print ("end of game")
                       
              
              

#Playable Bit



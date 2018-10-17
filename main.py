from folder import battleFight
from folder import charSel
import time
import sys

player1 = "None"
player2 = "None"
att1 = 0
att2 = 0
def1 = 0
def2 = 0
agt1 = 0
agt2 = 0
prompt = ""

#Intro Song
time.sleep(1)
print("I wanna be the very best...")
time.sleep(1)
print("Like no one ever was...")
time.sleep(1)
print("To catch them is my real test...")
time.sleep(1)
print("To train them is my cause...")
time.sleep(1)
print("Pokemon! Gotta catch 'em all!!!")
time.sleep(1)

#Title Screen
while prompt not in ("Y","y","N","n"):
    prompt = str(input("Start Game? (Y/N))  "))
#Enter Game
    if prompt in ("Y","y"):
#Player_1
        while (player1 == "None"):
            print("Player1: Choose your Pokemon!!!!")
            player1 = charSel.charSel()

#Player_2
        while (player2 == "None"):
            print("Player2: Choose your Pokemon!!!")
            player2 = charSel.charSel()

#Proceed to Battle
        if (player1 != "None" or player2 != "None"):
            print("\n")
            print("\n")
            battleFight.battleFight( str(player1), str(player2),1,1,1,1,1,1)
#Exit Command
    if prompt in ("N","n"):
        sys.exit()



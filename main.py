from folder import battleFight
from folder import PokeSelect
import time
import sys

player1 = "None"
player2 = "None"
data = ["","","",""]
att1 = ""
att2 = ""
def1 = ""
def2 = ""
agt1 = ""
agt2 = ""
spclmove1 = ""
spclmove2 = ""
winner = 0
prompt = ""
checker = True
dec = ""

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

print("===============================================")
print("####  #####  #  #  #####  #     #  #####  #   #")
print("#  #  #   #  # #   #      ##   ##  #   #  ##  #")
print("####  #   #  ##    #####  #  #  #  #   #  # # #")
print("#     #   #  # #   #      #     #  #   #  #  ##")
print("#     #####  #  #  #####  #     #  #####  #   #")
print("===============================================")
time.sleep(1)
print("Gotta catch'em all!!!")

#Title Screen
while prompt not in ("Y","y","N","n"):
  prompt = str(input("Start Game? (Y/N): "))
#Enter Game
  if prompt in ("Y","y"):
    #Player_1
    while checker:
      print("#############################################")
      print("Player1: Choose your Pokemon!!!!")
      data = PokeSelect.PokeSelect.PokeSelect()
      player1 = data[0]
      att1 = int(data[1])
      def1 = int(data[2])
      agt1 = int(data[3])
      spclmove1 = data[4]

      #Player_2
      print("Player2: Choose your Pokemon!!!")
      data = PokeSelect.PokeSelect.PokeSelect()
      player2 = data[0]
      att2 = int(data[1])
      def2 = int(data[2])
      agt2 = int(data[3])
      spclmove2 = data[4]
      #Proceed to Battle
      if (player1 != "None" or player2 != "None"):
        print("\n")
        print("\n")
        winner = battleFight.battleFight(str(player1), str(player2), att1, att2, def1, def2, agt1, agt2, spclmove1, spclmove2)
      
      y = input("Do you want to play again??[Y/N]")
      if(y == "y" or y == "Y"):
        checker = True
      else:
        checker == False
        sys.exit()
  #Exit Command
  elif prompt in ("N","n"):
        sys.exit()



from folder import battleFight
from folder import PokeSelect
import sys

player1 = "None"
player2 = "None"
att1 = 0
att2 = 0
def1 = 0
def2 = 0
agt1 = 0
agt2 = 0
winner = 0
check = True


#Player_1
while (player1 == "None"):
  player1 = PokeSelect.PokeSelect()
#Player_2
while (player2 == "None"):
  player2 = PokeSelect.PokeSelect()

battleFight.battleFight( str(player1), str(player2),1,1,1,1,1,1,winner)

print("Gameover")
if(winner == 1):
  print("Player 1 Wins!!!")
elif(winner == 2):
  print("Player 2 Wins!!!")
else:
  print("Error")
    
while check:
  Dec = str(input("Do you want to play again?[Y/N]"))
  if(Dec == "Y" or Dec == "y"):
  #Temporary
    print("Goto CharSel()")
    sys.exit()
    check = False
  elif(Dec == "N" or Dec == "n"):
    sys.exit()
    check = False
  else:
   print("Input not recognized.")
   check = True

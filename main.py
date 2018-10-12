from folder import battleFight
from folder import charSel

player1 = "None"
player2 = "None"
att1 = 0
att2 = 0
def1 = 0
def2 = 0
agt1 = 0
agt2 = 0


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

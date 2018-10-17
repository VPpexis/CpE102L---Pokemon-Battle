import random
import sys
import os
class battleFight():
  
    #Module for Player Movement
  def Player(Name, Att, Agt, P_potion, spclmove):
    move = 0
    potion = 0
    missMod = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Heal_up = False
    checker = True
    punch = random.randint(18,25)
    MegaPunch = random.randint(10,35)
    heal = random.randint(20,25)
    moves = {"Punch": punch, "MegaPunch": MegaPunch, "Heal": heal}

    while checker:
      if checker:
        move = int(input(Name + ", Please select move: \n 1.)Tackle \n 2.)%s \n 3.)Heal\n >" % spclmove))
      else:
        move = input(">")

      print("=============================================")
     #Miss Generator
      miss = random.randint(1,20)
      x = 0
     #Miss Modifier
      missMod[x] = missMod[x] + x

      while(Agt != x):
        x += 1
        missMod[x] = missMod[x] + x

      #Miss Decision
      if (move != 3):
        if miss in missMod:
          move = 0
          print("You missed.")
          return [move, Heal_up, potion]

      #Move Decision
      if(move == 1):
        move = moves["Punch"]
        Heal_up = False
        move = move + (Att/20)*move
        print("%s used Tackle and deals %d damage." % (Name, move))
        checker = False
      elif(move==2):
        move = moves["MegaPunch"]
        Heal_up = False
        checker = False
        move = move + (Att/20)*move
        print("%s used %s and deals %d damage." % (Name, spclmove, move))
      elif(move==3):
        if(P_potion != 0):
          move = moves["Heal"]
          Heal_up = True
          checker = False
          potion = -1
          print("%s used Potion and recovers %d HP" % (Name, move))
        else:
          checker = True
          print("No more Potion.")
      else:
        print("Input not recognized")
        checker = True
      

    return [move, Heal_up, potion]

  def __init__(self, p1, p2, Att1, Att2, Def1, Def2, Agt1, Agt2, spclmove1, spclmove2):
    #Variable Delcleraation
    self.p1 = p1
    self.p2 = p2
    self.Att1 = Att1
    self.Att2 = Att2
    self.Def1 = Def1
    self.Def2 = Def2
    self.Agt1 = Agt1
    self.Agt2 = Agt2
    self.spclmove1 = spclmove1
    self.spclmove2 = spclmove2
    Heal_up = False
    P1_HP = 100
    P2_HP = 100
    Base_HP1 = 0
    Base_HP2 = 0
    potion1 = 3
    potion2 = 3
    potionCounter1 = 0
    potionCounter2 = 0
    check = True
    turn = 0
    p_move = 0

    #Heatlh + Defense Calculations
    P1_HP = P1_HP + (Def1/20)*P1_HP
    Base_HP1 = P1_HP
    P2_HP = P2_HP + (Def2/20)*P2_HP
    Base_HP2 = P1_HP

    turn = random.randint(1,2)

    if(turn==1):
      print( p1 + " goes first!!")
    else:
      print(p2 + " goes first!!")

    while(P1_HP >= 0 and P2_HP >= 0):
      if(turn == 1):
        #P1 Turn
        print("#############################################")
        print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
        print("=============================================")
        print("%s's Potion: %d      \n%s's Potion: %d" % (p1,potion1,p2, potion2))
        p_move, Heal_up, potionCounter1 = battleFight.Player(p1, Att1, Agt2, potion1, spclmove1)
        potion1 += potionCounter1
        
        if(P1_HP <= 0 or P2_HP <= 0):
         break

        #Heal P1
        if Heal_up:
          P1_HP = P1_HP + p_move
          if(P1_HP > Base_HP1):
            P1_HP = Base_HP1
        else:
          P2_HP = P2_HP - p_move

        #P2 Turn
        print("#############################################")
        print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
        print("=============================================")
        print("%s's Potion: %d      \n%s's Potion: %d" % (p1,potion1,p2, potion2))
        p_move, Heal_up, potionCounter2 = battleFight.Player(p2, Att2, Agt1, potion2, spclmove2)
        potion2 += potionCounter2

        if(P1_HP <= 0 or P2_HP <= 0):
         break

        #Heal P1
        if Heal_up:
          P2_HP = P2_HP + p_move
          if(P2_HP > Base_HP2):
            P2_HP = Base_HP2
        else:
          P1_HP = P1_HP - p_move
        
        p_move = 0
      elif(turn == 2):
        #P2 Turn
        print("#############################################")
        print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
        print("=============================================")
        print("%s's Potion: %d      \n%s's Potion: %d" % (p1,potion1,p2, potion2))
        p_move, Heal_up, potionCounter2 = battleFight.Player(p2,  Att2, Agt1, potion2, spclmove2)
        potion2 += potionCounter2
        
        if(P1_HP <= 0 or P2_HP <= 0):
          break

        #Heal P1
        if Heal_up:
          P2_HP = P2_HP + p_move
          if(P2_HP > Base_HP2):
            P2_HP = Base_HP2
        else:
        #Damge P2
          P1_HP = P1_HP - p_move

        #P1 Turn
        print("#############################################")
        print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
        print("=============================================")
        print("%s's Potion: %d      \n%s's Potion: %d" % (p1,potion1,p2, potion2))
        p_move, Heal_up, potionCounter1 = battleFight.Player(p1, Att1, Agt2, potion1, spclmove1)
        potion1 += potionCounter1

        if(P1_HP <= 0 or P2_HP <= 0):
         break

        #Heal P1
        if Heal_up:
          P1_HP = P1_HP + p_move
          if(P1_HP > Base_HP1):
            P1_HP = Base_HP2
        else:
        #Damge P2
          P2_HP = P2_HP - p_move
      elif(P1_HP <= 0 or P2_HP <= 0):
        break
    
    #Game is finished
    if(P1_HP <= 0):
      P1_HP = 0 
      print("#############################################")
      print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
      print(p2 + " is the winner!!!")
      return 
    elif(P2_HP <= 0):
      P2_HP = 0
      print("#############################################")
      print("%s HP: %.2f     %s HP: %.2f" % (p1, P1_HP, p2, P2_HP))
      print(p1 + " is the winner!!!")
      return 
    else:
      self.winner = 0
    return 




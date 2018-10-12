import random
import sys

class battleFight():
  Heal_up = True
  def __init__(self, p1, p2, Att1, Att2, Def1, Def2, Agt1, Agt2):
    self.p1 = p1
    self.p2 = p2
    self.Att1 = Att1
    self.Att2 = Att2
    self.Def1 = Def1
    self.Def2 = Def2
    self.Agt1 = Agt1
    self.Agt2 = Agt2

    winner = "None"
    P1_HP = 100
    P2_HP = 100
    dec = "No"
    Heal_up = False
    check = True
    turn = 0
    p_move = 0

    P1_HP = P1_HP + (Def1/20)*P1_HP
    P2_HP = P2_HP + (Def2/20)*P2_HP

    turn = random.randint(1,2)

    if(turn==1):
      print("Player 1 goes first!!")
    else:
      print("Player 2 goes first!!")

    while(P1_HP >= 0 and P2_HP >= 0):
      if(turn == 1):
        #P1 Turn
        print(str(p1) + " HP: " + str(P1_HP) + "     " + str(p2) + " HP: " + str(P2_HP))
        p_move = self.Player(p1,Att1,Agt1)

        #Heal P1
        if Heal_up:
          P1_HP = P1_HP + p_move
          if(P1_HP < 100):
            P1_HP = 100
        else:
          P2_HP = P2_HP - p_move

        #P2 Turn
        print(str(p1) + " HP: " + str(P1_HP) + "     " + str(p2) + " HP: " + str(P2_HP))
        p_move = self.Player(p2,Att2,Agt2)

        #Heal P1
        if Heal_up:
          P2_HP = P2_HP + p_move
          if(P2_HP < 100):
            P2_HP = 100
        else:
          P1_HP = P1_HP - p_move
        
        p_move = 0
      else:
        #P2 Turn
        print(str(p1) + "HP: " + str(P1_HP) + "     " + str(p2) + "HP: " + str(P2_HP))
        p_move = self.Player(p2, Att2,Agt2)

        #Heal P1
        if Heal_up:
          P2_HP = P2_HP + p_move
          if(P2_HP < 100):
            P2_HP = 100
        else:
        #Damge P2
          P1_HP = P1_HP - p_move

        #P1 Turn
        print(str(p1) + "HP: " + str(P1_HP) + "     " + str(p2) + "HP: " + str(P2_HP))
        p_move = self.Player(p1,Att1,Agt1)

        #Heal P1
        if Heal_up:
          P1_HP = P1_HP + p_move
          if(P1_HP < 100):
            P1_HP = 100
        else:
        #Damge P2
          P2_HP = P2_HP - p_move
    
    #Game is finished
    print("Gameover")
    if(P1_HP <= 0):
      print(str(p2)+ " Wins!!!")
    else:
      print(str(p1) + "Wins!!!")
    
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



  def Player(p, Name, Att, Agt):
    p.Name = Name
    p.Att = Att
    p.Agt = Agt
    move = 0
    missMod = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = 0
    checker = True
    punch = random.randint(18,25)
    MegaPunch = random.randint(10,35)
    heal = random.randint(20,25)
    moves = {"Punch": punch, "MegaPunch": MegaPunch, "Heal": heal}

    move = int(input(p.Name + ", Please select move: \n 1.)Punch \n 2.)MegaPunch \n 3.)Heal\n"))

    #Miss Generator
    miss = random.randint(1,20)

    #Miss Modifier
    missMod[x] = missMod[x] + x
    while(Agt != x):
      x += 1
      missMod[x] = missMod[x] + x

    #Miss Decision
    if miss in missMod:
      move = 0
      print("You missed.")
      return move

    #Move Decision
    while checker:
      if(move == 1):
        move = moves["Punch"]
        Heal_up = False
        move = move + (Att/20)*move
        checker = False
      elif(move==2):
        move = moves["MegaPunch"]
        Heal_up = False
        checker = False
        move = move + (Att/20)*move
      elif(move==3):
        move = moves["Heal"]
        Heal_up = True
        checker = False
      else:
        print("Input not recognized")
        checker = True

    return move

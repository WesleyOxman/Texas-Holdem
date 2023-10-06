import random as rand



class TexasHoldem:
  def __init__(self):
    self.numPlayer = 0
    self.player4hand = []
  def getPlayerStart(self):
    self.playerStart = eval(input("How much do you want each player to start out with?: "))
    return self.playerStart
  def getstartingBet(self):
    self.startingbet = eval(input("How much would you like the starting bet to be?:"))
    return self.getstartingBet

  def playerHands(self):
    self.numPlayer = eval(input("How many players are there?: "))
    
    self.deck = ['ace_of_spades', 'ace_of_clubs', 'ace_of_diamonds', 'ace_of_hearts', 
         'two_of_spades', 'two_of_clubs', 'two_of_diamonds', 'two_of_hearts', 
         'three_of_spades', 'three_of_clubs', 'three_of_diamonds', 'three_of_hearts', 
         'four_of_spades', 'four_of_clubs', 'four_of_diamonds', 'four_of_hearts', 
         'five_of_spades', 'five_of_clubs', 'five_of_diamonds', 'five_of_hearts', 
         'six_of_spades', 'six_of_clubs', 'six_of_diamonds', 'six_of_hearts', 
         'seven_of_spades', 'seven_of_clubs', 'seven_of_diamonds', 'seven_of_hearts', 
         'eight_of_spades', 'eight_of_clubs', 'eight_of_diamonds', 'eight_of_hearts', 
         'nine_of_spades', 'nine_of_clubs', 'nine_of_diamonds', 'nine_of_hearts', 
         'ten_of_spades', 'ten_of_clubs', 'ten_of_diamonds', 'ten_of_hearts', 
         'jack_of_spades', 'jack_of_clubs', 'jack_of_diamonds', 'jack_of_hearts', 
         'queen_of_spades', 'queen_of_clubs', 'queen_of_diamonds', 'queen_of_hearts', 
         'king_of_spades', 'king_of_clubs', 'king_of_diamonds', 'king_of_hearts']
    rand.shuffle(self.deck)
    
    if self.numPlayer >= 1:
      self.player1hand = []
      self.p1card1 = self.deck[0]
      self.player1hand.append(self.p1card1)
      self.p1card2 = self.deck[self.numPlayer]
      self.player1hand.append(self.p1card2)
      self.deck.remove(self.p1card1)
      self.deck.remove(self.p1card2)
      self.MoneyP1 = self.playerStart
      self.player1 = 1
      
    if self.numPlayer >= 2:
      self.player2hand = []
      self.p2card1 = self.deck[1]
      self.player2hand.append(self.p2card1)
      self.p2card2 = self.deck[self.numPlayer+1]
      self.player2hand.append(self.p2card2)
      self.deck.remove(self.p2card1)
      self.deck.remove(self.p2card2)
      self.MoneyP2 = self.playerStart - (self.startingbet/2)
      self.player2 = 1

    if self.numPlayer >= 3:
      self.player3hand = []
      self.p3card1 = self.deck[2]
      self.player3hand.append(self.p3card1)
      self.p3card2 = self.deck[self.numPlayer+2]
      self.player3hand.append(self.p3card2)
      self.deck.remove(self.p3card1)
      self.deck.remove(self.p3card2)
      self.MoneyP3 = self.playerStart - (self.startingbet)
      self.player3 = 1

    if self.numPlayer >= 4:
      self.p4card1 = self.deck[3]
      self.player4hand.append(self.p4card1)
      self.p4card2 = self.deck[self.numPlayer+3]
      self.player4hand.append(self.p4card2)
      self.deck.remove(self.p4card1)
      self.deck.remove(self.p4card2)
      self.MoneyP4 = self.playerStart
      self.player4 = 1
      
    if self.numPlayer >= 5:
      self.player5hand = []
      self.p5card1 = self.deck[4]
      self.player5hand.append(self.p5card1)
      self.p5card2 = self.deck[self.numPlayer+4]
      self.player5hand.append(self.p5card2)
      self.deck.remove(self.p5card1)
      self.deck.remove(self.p5card2)
      self.MoneyP5 = self.playerStart
      self.player5 = 1
      
    if self.numPlayer >= 6:
      self.player6hand = []
      self.p6card1 = self.deck[5]
      self.player6hand.append(self.p6card1)
      self.p6card2 = self.deck[self.numPlayer+5]
      self.player6hand.append(self.p6card2)
      self.deck.remove(self.p6card1)
      self.deck.remove(self.p6card2)
      self.MoneyP6 = self.playerStart
      self.player6 = 1
      
    if self.numPlayer >= 7:
      self.player7hand = []
      self.p7card1 = self.deck[6]
      self.player7hand.append(self.p7card1)
      self.p7card2 = self.deck[self.numPlayer+6]
      self.player7hand.append(self.p7card2)
      self.deck.remove(self.p7card1)
      self.deck.remove(self.p7card2)
      self.MoneyP7 = self.playerStart
      self.player7 = 1
      
    if self.numPlayer >= 8:
      self.player8hand = []
      self.p8card1 = self.deck[7]
      self.player8hand.append(self.p8card1)
      self.p8card2 = self.deck[self.numPlayer+7]
      self.player8hand.append(self.p8card2)
      self.deck.remove(self.p8card1)
      self.deck.remove(self.p8card2)
      self.MoneyP8 = self.playerStart
      self.player8 = 1
      
    if self.numPlayer >= 9:
      self.player9hand = []
      self.p9card1 = self.deck[8]
      self.player9hand.append(self.p9card1)
      self.p9card2 = self.deck[self.numPlayer+8]
      self.player10hand.append(self.p10card2)
      self.deck.remove(self.p9card1)
      self.deck.remove(self.p9card2)
      self.MoneyP9 = self.playerStart
      self.player9 = 1
      
    if self.numPlayer >= 10:
      self.player10hand = []
      self.p10card1 = self.deck[9]
      self.player10hand.append(self.p10card1)
      self.p10card2 = self.deck[self.numPlayer+9]
      self.player10hand.append(self.p10card2)
      self.deck.remove(self.p10card1)
      self.deck.remove(self.p10card2)
      self.MoneyP10 = self.playerStart
      self.player10 = 1
      
    if self.numPlayer >= 11:
      self.player11hand = []
      self.p11card1 = self.deck[10]
      self.player11hand.append(self.p11card1)
      self.p11card2 = self.deck[self.numPlayer+10]
      self.player11hand.append(self.p11card2)
      self.deck.remove(self.p11card1)
      self.deck.remove(self.p11card2)
      self.MoneyP11 = self.playerStart
      self.player11 = 1
      
    if self.numPlayer >= 12:
      self.player12hand = []
      self.p12card1 = self.deck[11]
      self.player12hand.append(self.p12card1)
      self.p12card2 = self.deck[self.numPlayer+11]
      self.player12hand.append(self.p12card2)
      self.deck.remove(self.p12card1)
      self.deck.remove(self.p12card2)
      self.MoneyP12 = self.playerStart
      self.player12 = 1
      
    if self.numPlayer >= 13:
      self.player13hand = []
      self.p13card1 = self.deck[12]
      self.player13hand.append(self.p13card1)
      self.p4card2 = self.deck[self.numPlayer+12]
      self.player13hand.append(self.p13card2)
      self.deck.remove(self.p13card1)
      self.deck.remove(self.p13card2)
      self.MoneyP13 = self.playerStart
      self.player13 = 1
      
    if self.numPlayer >= 14:
      self.player14hand = []
      self.p13card1 = self.deck[13]
      self.player14hand.append(self.p14card1)
      self.p4card2 = self.deck[self.numPlayer+13]
      self.player14hand.append(self.p14card2)
      self.deck.remove(self.p14card1)
      self.deck.remove(self.p14card2)
      self.MoneyP14 = self.playerStart
      self.player14 = 1
      
    if self.numPlayer >= 15:
      self.player15hand = []
      self.p13card1 = self.deck[14]
      self.player15hand.append(self.p15card1)
      self.p4card2 = self.deck[self.numPlayer+14]
      self.player15hand.append(self.p15card2)
      self.deck.remove(self.p15card1)
      self.deck.remove(self.p15card2)
      self.MoneyP15 = self.playerStart
      self.player15 = 1
      
    if self.numPlayer >= 16:
      self.player16hand = []
      self.p13card1 = self.deck[15]
      self.player16hand.append(self.p16card1)
      self.p4card2 = self.deck[self.numPlayer+15]
      self.player16hand.append(self.p16card2)
      self.deck.remove(self.p16card1)
      self.deck.remove(self.p16card2)
      self.MoneyP16 = self.playerStart
      self.player16 = 1
      
    if self.numPlayer >= 17:
      self.player17hand = []
      self.p13card1 = self.deck[16]
      self.player17hand.append(self.p17card1)
      self.p4card2 = self.deck[self.numPlayer+16]
      self.player17hand.append(self.p17card2)
      self.deck.remove(self.p17card1)
      self.deck.remove(self.p17card2)
      self.MoneyP17 = self.playerStart
      self.player17 = 1
      
    if self.numPlayer >= 18:
      self.player18hand = []
      self.p13card1 = self.deck[17]
      self.player18hand.append(self.p18card1)
      self.p4card2 = self.deck[self.numPlayer+17]
      self.player18hand.append(self.p18card2)
      self.deck.remove(self.p18card1)
      self.deck.remove(self.p18card2)
      self.MoneyP18 = self.playerStart
      self.player18 = 1
      
    if self.numPlayer >= 19:
      self.player19hand = []
      self.p13card1 = self.deck[18]
      self.player19hand.append(self.p19card1)
      self.p4card2 = self.deck[self.numPlayer+18]
      self.player19hand.append(self.p19card2)
      self.deck.remove(self.p19card1)
      self.deck.remove(self.p19card2)
      self.MoneyP19 = self.playerStart
      self.player19 = 1
      
    if self.numPlayer >= 20:
      self.player20hand = []
      self.p13card1 = self.deck[19]
      self.player20hand.append(self.p20card1)
      self.p4card2 = self.deck[self.numPlayer+19]
      self.player20hand.append(self.p20card2)
      self.deck.remove(self.p20card1)
      self.deck.remove(self.p20card2)
      self.MoneyP20 = self.playerStart
      self.player20 = 1
      
    if self.numPlayer >= 21:
      self.player21hand = []
      self.p13card1 = self.deck[20]
      self.player21hand.append(self.p21card1)
      self.p4card2 = self.deck[self.numPlayer+20]
      self.player21hand.append(self.p21card2)
      self.deck.remove(self.p21card1)
      self.deck.remove(self.p21card2)
      self.MoneyP21 = self.playerStar
      self.player21 = 1
      
    if self.numPlayer >= 22:
      self.player22hand = []
      self.p13card1 = self.deck[21]
      self.player22hand.append(self.p22card1)
      self.p4card2 = self.deck[self.numPlayer+21]
      self.player22hand.append(self.p22card2)
      self.deck.remove(self.p22card1)
      self.deck.remove(self.p22card2)
      self.MoneyP22 = self.playerStart
      self.player1 = 1

  def startingRound(self):
    if self.numPlayer >= 4:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("Player 4 what would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP4 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP4)
      if self.pChoice == "fold":
        self.player4 = 0
        print("player has folded")

    if self.numPlayer >= 5:
      print("\nplayer 5 your cards are", self.player5hand)
      self.pChoice = input("Player 5 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP5 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP5)
      if self.pChoice == "fold":
        self.player5 = 0
        print("player has folded")

    if self.numPlayer >= 6:
      print("\nplayer 6 your cards are", self.player6hand)
      self.pChoice = input("Player 6 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP6 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP6)
      if self.pChoice == "fold":
        self.playeR6 = 0
        print("player has folded")

    if self.numPlayer >= 7:
      print("\nplayer 7 your cards are", self.player7hand)
      self.pChoice = input("Player 7 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP7 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP7)
      if self.pChoice == "fold":
        self.player7 = 0
        print("player has folded")

    if self.numPlayer >= 8:
      print("\nplayer 8 your cards are", self.player8hand)
      self.pChoice = input("Player 8 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP8 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP8)
      if self.pChoice == "fold":
        self.player8 = 0
        print("player has folded")

    if self.numPlayer >= 9:
      print("\nplayer 9 your cards are", self.player9hand)
      self.pChoice = input("Player 9 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP9 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP9)
      if self.pChoice == "fold":
        self.player9 = 0
        print("player has folded")

    if self.numPlayer >= 10:
      print("\nplayer 10 your cards are", self.player10hand)
      self.pChoice = input("Player 10 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP10 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP10)
      if self.pChoice == "fold":
        self.player10 = 0
        print("player has folded")

    if self.numPlayer >= 11:
      print("\nplayer 11 your cards are", self.player11hand)
      self.pChoice = input("Player 11 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP11 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP11)
      if self.pChoice == "fold":
        self.player11 = 0
        print("player has folded")

    if self.numPlayer >= 12:
      print("\nplayer 12 your cards are", self.player12hand)
      self.pChoice = input("Player 12 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP12 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP12)
      if self.pChoice == "fold":
        self.player12 = 0
        print("player has folded")

    if self.numPlayer >= 13:
      print("\nplayer 13 your cards are", self.player13hand)
      self.pChoice = input("Player 13 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP13 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP13)
      if self.pChoice == "fold":
        self.player13 = 0
        print("player has folded")

    if self.numPlayer >= 14:
      print("\nlayer 14 your cards are", self.player14hand)
      self.pChoice = input("Player 14 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP14 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP14)
      if self.pChoice == "fold":
        self.player14 = 0
        print("player has folded")

    if self.numPlayer >= 15:
      print("\nplayer 15 your cards are", self.player15hand)
      self.pChoice = input("Player 15 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP15 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP15)
      if self.pChoice == "fold":
        self.player15 = 0
        print("player has folded")

    if self.numPlayer >= 16:
      print("\nplayer 16 your cards are", self.player16hand)
      self.pChoice = input("Player 16 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP16 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP16)
      if self.pChoice == "fold":
        self.player16 = 0
        print("player has folded")

    if self.numPlayer >= 17:
      print("\nplayer 17 your cards are", self.player17hand)
      self.pChoice = input("Player 17 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.Moneyp17 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP17)
      if self.pChoice == "fold":
        self.player17 = 0
        print("player has folded")

    if self.numPlayer >= 18:
      print("\nplayer 18 your cards are", self.player18hand)
      self.pChoice = input("Player 18 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP18 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP18)
      if self.pChoice == "fold":
        self.player18 = 0
        print("player has folded")

    if self.numPlayer >= 19:
      print("\nplayer 19 your cards are", self.player19hand)
      self.pChoice = input("Player 19 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP19 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP19)
      if self.pChoice == "fold":
        self.player19 = 0
        print("player has folded")

    if self.numPlayer >= 20:
      print("\nplayer 20 your cards are", self.player20hand)
      self.pChoice = input("Player 20 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP20 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP20)
      if self.pChoice == "fold":
        self.player20 = 0
        print("player has folded")

    if self.numPlayer >= 21:
      print("\nplayer 21 your cards are", self.player21hand)
      self.pChoice = input("Player 21 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP21 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP21)
      if self.pChoice == "fold":
        self.player21 = 0
        print("player has folded")

    if self.numPlayer >= 22:
      print("\nplayer 22 your cards are", self.player22hand)
      self.pChoice = input("Player 22 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP22 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP22)
      if self.pChoice == "fold":
        self.player22 = 0
        print("player has folded")

    if self.numPlayer >= 1:
      print("\nplayer 1 your cards are", self.player1hand)
      self.pChoice = input("Player 1 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP1 -= self.startingbet
        print("player has called")
        print("player your money is", self.MoneyP1)
      if self.pChoice == "fold":
        self.player1 = 0
        print("player has folded")

    if self.numPlayer >= 2:
      print("\nplayer 2 your cards are", self.player2hand)
      self.pChoice = input("Player 2 What would you like to do? You can call or fold: ")
      if self.pChoice == "call":
        self.MoneyP2 -= (self.startingbet/2)
        print("player has called")
        print("player your money is", self.MoneyP2)
      if self.pChoice == "fold":
        self.player2 = 0
        print("player has folded")

    if self.numPlayer >= 3:
      print("\nplayer 3 your cards are", self.player3hand)
      self.pChoice = print("Player 3 you can only check")
      print("player your money is", self.MoneyP3)



  def roundFlop(self):
  
    self.withbet1 = 0
    self.withbet2 = 0
    self.withbet3 = 0
    self.withbet4 = 0
    self.withbet5 = 0
    self.withbet6 = 0
    self.withbet7 = 0
    self.withbet8 = 0
    self.withbet9 = 0
    self.withbet10 = 0
    self.withbet11 = 0
    self.withbet12 = 0
    self.withbet13 = 0
    self.withbet14 = 0
    self.withbet15 = 0
    self.withbet16 = 0
    self.withbet17 = 0
    self.withbet18 = 0
    self.withbet19 = 0
    self.withbet20 = 0
    self.withbet21 = 0
    self.withbet22 = 0

    self.betmade = 0
    print("\nthe first three community cards are", self.deck[0], self.deck[1], self.deck[2])
    self.deck.remove(self.deck[0])
    self.deck.remove(self.deck[1])
    self.deck.remove(self.deck[2])
    if self.numPlayer >= 4 and self.player4 == 1:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("What would you like to do? You can bet or check,")
      if self.pChoice == "bet":
        print("player has betted")
        self.betAmount = eval(input("what would you like to bet?: "))
        self.MoneyP4 -= self.betAmount
        print("player your money is", self.MoneyP4)
        self.betmade = 1
      if self.pChoice == "check":
        print("player has checked")
        print("player your money is", self.MoneyP4)

    if self.numPlayer >= 5 and self.player5 == 1:
      print("\nplayer 5 your cards are", self.player5hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.betmade = 1
          self.withbet5 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1

    if self.numPlayer >= 6 and self.player6 == 1:
      print("\nplayer 6 your cards are", self.player6hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.betmade = 1
          self.withbet6 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if self.numPlayer >= 7 and self.player7 == 1:
      print("\nplayer 7 your cards are", self.player7hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.betmade = 1
          self.withbet7 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if self.numPlayer >= 8 and self.player8 == 1:
      print("\nplayer 8 your cards are", self.player8hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.betmade = 1
          self.withbet8 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.withbet8 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if self.numPlayer >= 9 and self.player9 == 1:
      print("\nplayer 9 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.betmade = 1
          self.withbet9 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if self.numPlayer >= 10 and self.player10 == 1:
      print("\nplayer 10 your cards are", self.player10hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.betmade = 1
          self.withbet10 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if self.numPlayer >= 11 and self.player11 == 1:
      print("\nplayer 11 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.betmade = 1
          self.withbet11 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.withbet11 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if self.numPlayer >= 12 and self.player12 == 1:
      print("\nplayer 12 your cards are", self.player12hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if self.numPlayer >= 13 and self.player13 == 1:
      print("\nplayer 13 your cards are", self.player13hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet12 = 1

    if self.numPlayer >= 14 and self.player14 == 1:
      print("\nplayer 14 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.betmade = 1
          self.withbet14 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if self.numPlayer >= 15 and self.player15 == 1:
      print("\nplayer 15 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.betmade = 1
          self.withbet15 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if self.numPlayer >= 16 and self.player16 == 1:
      print("\nplayer 16 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.betmade = 1
          self.withbet16 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if self.numPlayer >= 17 and self.player17 == 1:
      print("\nplayer 17 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP4)
          self.betmade = 1
          self.withbet17 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if self.numPlayer >= 18 and self.player18 == 1:
      print("\nplayer 18 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.betmade = 1
          self.withbet18 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if self.numPlayer >= 19 and self.player19 == 1:
      print("\nplayer 19 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if self.numPlayer >= 20 and self.player20 == 1:
      print("\nplayer 20 your cards are", self.player20hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet19 = 1

    if self.numPlayer >= 21 and self.player21 == 1:
      print("\nplayer 21 your cards are", self.player21hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.betmade = 1
          self.withbet21 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if self.numPlayer >= 22 and self.player22 == 1:
      print("\nplayer 22 your cards are", self.player22hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.betmade = 1
          self.withbet22 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22= 1

    if self.numPlayer >= 1 and self.player1 == 1:
      print("\nplayer 1 your cards are", self.player1hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.betmade = 1
          self.withbet1 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if self.numPlayer >= 2 and self.player2 == 1:
      print("\nplayer 2 your cards are", self.player2hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.betmade = 1
          self.withbet2 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if self.numPlayer >= 3 and self.player3 == 1:
      print("\nplayer 3 your cards are", self.player3hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.betmade = 1
          self.withbet3 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP3)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1

    if self.numPlayer >= 4 and self.player4 == 1 and self.withbet4 != 1:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP4)
          self.withbet4 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player4 = 0
          self.withbet4 = 1
    
    if self.numPlayer >= 5 and self.player5 == 1 and self.withbet5 != 1:
      print("\nplayer 5 your cards are", self.player5hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1
      
    if self.numPlayer >= 6 and self.player6 == 1 and self.withbet6 != 1:
      print("\nplayer 6 your cards are", self.player6hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if  self.numPlayer >= 7 and self.player7 == 1 and self.withbet7 != 1:
      print("\nplayer 7 your cards are", self.player7hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if  self.numPlayer >= 8 and self.player8 == 1 and self.withbet8 != 1:
      print("\nplayer 8 your cards are", self.player8hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet8 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if  self.numPlayer >= 9 and self.player9 == 1 and self.withbet9 != 1:
      print("\nplayer 9 your cards are", self.player9hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if  self.numPlayer >= 10 and self.player10 == 1 and self.withbet10 != 1:
      print("\nplayer 10 your cards are", self.player10hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if  self.numPlayer >= 11 and self.player11 == 1 and self.withbet11 != 1:
      print("\nplayer 11 your cards are", self.player11hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet11 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if  self.numPlayer >= 12 and self.player12 == 1 and self.withbet12 != 1:
      print("\nplayer 12 your cards are", self.player12hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet12 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if  self.numPlayer >= 13 and self.player13 == 1 and self.withbet13 != 1:
      print("\nplayer 13 your cards are", self.player13hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet13 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet13 = 1\

    if  self.numPlayer >= 14 and self.player14 == 1 and self.withbet14 != 1:
      print("\nplayer 14 your cards are", self.player14hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if  self.numPlayer >= 15 and self.player6 == 15 and self.withbet15 != 1:
      print("\nplayer 15 your cards are", self.player15hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if  self.numPlayer >= 16 and self.player16 == 1 and self.withbet16 != 1:
      print("\nplayer 16 your cards are", self.player16hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if  self.numPlayer >= 17 and self.player17 == 1 and self.withbet17 != 1:
      print("\nplayer 17 your cards are", self.player17hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if  self.numPlayer >= 18 and self.player18 == 1 and self.withbet18 != 1:
      print("\nplayer 18 your cards are", self.player18hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if  self.numPlayer >= 19 and self.player19 == 1 and self.withbet19 != 1:
      print("\nplayer 19 your cards are", self.player19hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if  self.numPlayer >= 20 and self.player20 == 1 and self.withbet20 != 1:
      print("\nplayer 20 your cards are", self.player20hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet20 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet20 = 1

    if  self.numPlayer >= 21 and self.player21 == 1 and self.withbet21 != 1:
      print("\nplayer 21 your cards are", self.player21hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if  self.numPlayer >= 22 and self.player22 == 1 and self.withbet22 != 1:
      print("\nplayer 22 your cards are", self.player22hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22 = 1

    if  self.numPlayer >= 1 and self.player1 == 1 and self.withbet1 != 1:
      print("\nplayer 1 your cards are", self.player1hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if  self.numPlayer >= 2 and self.player2 == 1 and self.withbet2 != 1:
      print("\nplayer 2 your cards are", self.player2hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if  self.numPlayer >= 3 and self.player3 == 1 and self.withbet3 != 1:
      print("\nplayer 3 your cards are", self.player3hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1

  def roundTurn(self):
    self.betmade = 0
    print("\nthe turn card is", self.deck[0])
    self.deck.remove(self.deck[0])
    
    if self.numPlayer >= 4 and self.player4 == 1:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("What would you like to do? You can bet or check,")
      if self.pChoice == "bet":
        print("player has betted")
        self.betAmount = eval(input("what would you like to bet?: "))
        self.MoneyP4 -= self.betAmount
        print("player your money is", self.MoneyP4)
        self.betmade = 1
      if self.pChoice == "check":
        print("player has checked")
        print("player your money is", self.MoneyP4)

    if self.numPlayer >= 5 and self.player5 == 1:
      print("\nplayer 5 your cards are", self.player5hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.betmade = 1
          self.withbet5 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1

    if self.numPlayer >= 6 and self.player6 == 1:
      print("\nplayer 6 your cards are", self.player6hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.betmade = 1
          self.withbet6 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if self.numPlayer >= 7 and self.player7 == 1:
      print("\nplayer 7 your cards are", self.player7hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.betmade = 1
          self.withbet7 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if self.numPlayer >= 8 and self.player8 == 1:
      print("\nplayer 8 your cards are", self.player8hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.betmade = 1
          self.withbet8 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.withbet8 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if self.numPlayer >= 9 and self.player9 == 1:
      print("\nplayer 9 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.betmade = 1
          self.withbet9 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if self.numPlayer >= 10 and self.player10 == 1:
      print("\nplayer 10 your cards are", self.player10hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.betmade = 1
          self.withbet10 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if self.numPlayer >= 11 and self.player11 == 1:
      print("\nplayer 11 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.betmade = 1
          self.withbet11 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.withbet11 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if self.numPlayer >= 12 and self.player12 == 1:
      print("\nplayer 12 your cards are", self.player12hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if self.numPlayer >= 13 and self.player13 == 1:
      print("\nplayer 13 your cards are", self.player13hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet12 = 1

    if self.numPlayer >= 14 and self.player14 == 1:
      print("\nplayer 14 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.betmade = 1
          self.withbet14 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if self.numPlayer >= 15 and self.player15 == 1:
      print("\nplayer 15 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.betmade = 1
          self.withbet15 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if self.numPlayer >= 16 and self.player16 == 1:
      print("\nplayer 16 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.betmade = 1
          self.withbet16 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if self.numPlayer >= 17 and self.player17 == 1:
      print("\nplayer 17 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP4)
          self.betmade = 1
          self.withbet17 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if self.numPlayer >= 18 and self.player18 == 1:
      print("\nplayer 18 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.betmade = 1
          self.withbet18 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if self.numPlayer >= 19 and self.player19 == 1:
      print("\nplayer 19 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if self.numPlayer >= 20 and self.player20 == 1:
      print("\nplayer 20 your cards are", self.player20hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet19 = 1

    if self.numPlayer >= 21 and self.player21 == 1:
      print("\nplayer 21 your cards are", self.player21hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.betmade = 1
          self.withbet21 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if self.numPlayer >= 22 and self.player22 == 1:
      print("\nplayer 22 your cards are", self.player22hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.betmade = 1
          self.withbet22 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22= 1

    if self.numPlayer >= 1 and self.player1 == 1:
      print("\nplayer 1 your cards are", self.player1hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.betmade = 1
          self.withbet1 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if self.numPlayer >= 2 and self.player2 == 1:
      print("\nplayer 2 your cards are", self.player2hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.betmade = 1
          self.withbet2 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if self.numPlayer >= 3 and self.player3 == 1:
      print("\nplayer 3 your cards are", self.player3hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.betmade = 1
          self.withbet3 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP3)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1

    if self.numPlayer >= 4 and self.player4 == 1 and self.withbet4 != 1:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
        print("player has called")
        self.MoneyP4 -= self.betAmount
        print("player your money is", self.MoneyP4)
        self.withbet4 = 1
      if self.pChoice == "fold":
        print("player has folded")
        self.player5 = 0
        self.withbet4 = 1
    
    if self.numPlayer >= 5 and self.player5 == 1 and self.withbet5 != 1:
      print("\nplayer 5 your cards are", self.player5hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1
      
    if self.numPlayer >= 6 and self.player6 == 1 and self.withbet6 != 1:
      print("\nplayer 6 your cards are", self.player6hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if  self.numPlayer >= 7 and self.player7 == 1 and self.withbet7 != 1:
      print("\nplayer 7 your cards are", self.player7hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if  self.numPlayer >= 8 and self.player8 == 1 and self.withbet8 != 1:
      print("\nplayer 8 your cards are", self.player8hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet8 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if  self.numPlayer >= 9 and self.player9 == 1 and self.withbet9 != 1:
      print("\nplayer 9 your cards are", self.player9hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if  self.numPlayer >= 10 and self.player10 == 1 and self.withbet10 != 1:
      print("\nplayer 10 your cards are", self.player10hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if  self.numPlayer >= 11 and self.player11 == 1 and self.withbet11 != 1:
      print("\nplayer 11 your cards are", self.player11hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet11 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if  self.numPlayer >= 12 and self.player12 == 1 and self.withbet12 != 1:
      print("\nplayer 12 your cards are", self.player12hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet12 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if  self.numPlayer >= 13 and self.player13 == 1 and self.withbet13 != 1:
      print("\nplayer 13 your cards are", self.player13hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet13 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet13 = 1\

    if  self.numPlayer >= 14 and self.player14 == 1 and self.withbet14 != 1:
      print("\nplayer 14 your cards are", self.player14hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if  self.numPlayer >= 15 and self.player6 == 15 and self.withbet15 != 1:
      print("\nplayer 15 your cards are", self.player15hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if  self.numPlayer >= 16 and self.player16 == 1 and self.withbet16 != 1:
      print("\nplayer 16 your cards are", self.player16hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if  self.numPlayer >= 17 and self.player17 == 1 and self.withbet17 != 1:
      print("\nplayer 17 your cards are", self.player17hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if  self.numPlayer >= 18 and self.player18 == 1 and self.withbet18 != 1:
      print("\nplayer 18 your cards are", self.player18hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if  self.numPlayer >= 19 and self.player19 == 1 and self.withbet19 != 1:
      print("\nplayer 19 your cards are", self.player19hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if  self.numPlayer >= 20 and self.player20 == 1 and self.withbet20 != 1:
      print("\nplayer 20 your cards are", self.player20hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet20 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet20 = 1

    if  self.numPlayer >= 21 and self.player21 == 1 and self.withbet21 != 1:
      print("\nplayer 21 your cards are", self.player21hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if  self.numPlayer >= 22 and self.player22 == 1 and self.withbet22 != 1:
      print("\nplayer 22 your cards are", self.player22hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22 = 1

    if  self.numPlayer >= 1 and self.player1 == 1 and self.withbet1 != 1:
      print("\nplayer 1 your cards are", self.player1hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if  self.numPlayer >= 2 and self.player2 == 1 and self.withbet2 != 1:
      print("\nplayer 2 your cards are", self.player2hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if  self.numPlayer >= 3 and self.player3 == 1 and self.withbet3 != 1:
      print("\nplayer 3 your cards are", self.player3hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1

  def roundRiver(self):
    self.betmade = 0
    print("\nthe river cards is", self.deck[0])
    self.deck.remove(self.deck[0])
    if self.numPlayer >= 4 and self.player4 == 1:
      print("\nplayer 4 your cards are", self.player4hand)
      self.pChoice = input("What would you like to do? You can bet or check,")
      if self.pChoice == "bet":
        print("player has betted")
        self.betAmount = eval(input("what would you like to bet?: "))
        self.MoneyP4 -= self.betAmount
        print("player your money is", self.MoneyP4)
        self.betmade = 1
      if self.pChoice == "check":
        print("player has checked")
        print("player your money is", self.MoneyP4)

    if self.numPlayer >= 5 and self.player5 == 1:
      print("\nplayer 5 your cards are", self.player5hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.betmade = 1
          self.withbet5 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1

    if self.numPlayer >= 6 and self.player6 == 1:
      print("\nplayer 6 your cards are", self.player6hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.betmade = 1
          self.withbet6 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if self.numPlayer >= 7 and self.player7 == 1:
      print("\nplayer 7 your cards are", self.player7hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.betmade = 1
          self.withbet7 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if self.numPlayer >= 8 and self.player8 == 1:
      print("\nplayer 8 your cards are", self.player8hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.betmade = 1
          self.withbet8 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP8)
          self.withbet8 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if self.numPlayer >= 9 and self.player9 == 1:
      print("\nplayer 9 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.betmade = 1
          self.withbet9 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if self.numPlayer >= 10 and self.player10 == 1:
      print("\nplayer 10 your cards are", self.player10hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.betmade = 1
          self.withbet10 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if self.numPlayer >= 11 and self.player11 == 1:
      print("\nplayer 11 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.betmade = 1
          self.withbet11 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP11)
          self.withbet11 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if self.numPlayer >= 12 and self.player12 == 1:
      print("\nplayer 12 your cards are", self.player12hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP12)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if self.numPlayer >= 13 and self.player13 == 1:
      print("\nplayer 13 your cards are", self.player13hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.betmade = 1
          self.withbet12 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet12 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet12 = 1

    if self.numPlayer >= 14 and self.player14 == 1:
      print("\nplayer 14 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.betmade = 1
          self.withbet14 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if self.numPlayer >= 15 and self.player15 == 1:
      print("\nplayer 15 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.betmade = 1
          self.withbet15 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if self.numPlayer >= 16 and self.player16 == 1:
      print("\nplayer 16 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.betmade = 1
          self.withbet16 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if self.numPlayer >= 17 and self.player17 == 1:
      print("\nplayer 17 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP4)
          self.betmade = 1
          self.withbet17 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if self.numPlayer >= 18 and self.player18 == 1:
      print("\nplayer 18 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.betmade = 1
          self.withbet18 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if self.numPlayer >= 19 and self.player19 == 1:
      print("\nplayer 19 your cards are", self.player4hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if self.numPlayer >= 20 and self.player20 == 1:
      print("\nplayer 20 your cards are", self.player20hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP4 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.betmade = 1
          self.withbet19 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet19 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet19 = 1

    if self.numPlayer >= 21 and self.player21 == 1:
      print("\nplayer 21 your cards are", self.player21hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.betmade = 1
          self.withbet21 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if self.numPlayer >= 22 and self.player22 == 1:
      print("\nplayer 22 your cards are", self.player22hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.betmade = 1
          self.withbet22 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22= 1

    if self.numPlayer >= 1 and self.player1 == 1:
      print("\nplayer 1 your cards are", self.player1hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.betmade = 1
          self.withbet1 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if self.numPlayer >= 2 and self.player2 == 1:
      print("\nplayer 2 your cards are", self.player2hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.betmade = 1
          self.withbet2 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP4)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if self.numPlayer >= 3 and self.player3 == 1:
      print("\nplayer 3 your cards are", self.player3hand)
      if self.betmade == 0:
        self.pChoice = input("What would you like to do? You can bet or check,")
        if self.pChoice == "bet":
          print("player has betted")
          self.betAmount = eval(input("what would you like to bet?: "))
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.betmade = 1
          self.withbet3 = 1
        if self.pChoice == "check":
          print("player has checked")
          print("player your money is", self.MoneyP3)
      else:
        self.pChoice = input("What would you like to do? You can call or fold,")
        if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
        if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1

    if self.numPlayer >= 4 and self.player4 == 1 and self.withbet4 != 1:
      print("\nplayer 4 your cards are", self.player5hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1

    if self.numPlayer >= 5 and self.player5 == 1 and self.withbet5 != 1:
      print("\nplayer 5 your cards are", self.player5hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP5 -= self.betAmount
          print("player your money is", self.MoneyP5)
          self.withbet5 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player5 = 0
          self.withbet5 = 1
      
    if self.numPlayer >= 6 and self.player6 == 1 and self.withbet6 != 1:
      print("\nplayer 6 your cards are", self.player6hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP6 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet6 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player6 = 0
          self.withbet6 = 1

    if  self.numPlayer >= 7 and self.player7 == 1 and self.withbet7 != 1:
      print("\nplayer 7 your cards are", self.player7hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP7 -= self.betAmount
          print("player your money is", self.MoneyP7)
          self.withbet7 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player7 = 0
          self.withbet7 = 1

    if  self.numPlayer >= 8 and self.player8 == 1 and self.withbet8 != 1:
      print("\nplayer 8 your cards are", self.player8hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP8 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet8 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player8 = 0
          self.withbet8 = 1

    if  self.numPlayer >= 9 and self.player9 == 1 and self.withbet9 != 1:
      print("\nplayer 9 your cards are", self.player9hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP9 -= self.betAmount
          print("player your money is", self.MoneyP9)
          self.withbet9 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player9 = 0
          self.withbet9 = 1

    if  self.numPlayer >= 10 and self.player10 == 1 and self.withbet10 != 1:
      print("\nplayer 10 your cards are", self.player10hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP10 -= self.betAmount
          print("player your money is", self.MoneyP10)
          self.withbet10 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player10 = 0
          self.withbet10 = 1

    if  self.numPlayer >= 11 and self.player11 == 1 and self.withbet11 != 1:
      print("\nplayer 11 your cards are", self.player11hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP11 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet11 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player11 = 0
          self.withbet11 = 1

    if  self.numPlayer >= 12 and self.player12 == 1 and self.withbet12 != 1:
      print("\nplayer 12 your cards are", self.player12hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP12 -= self.betAmount
          print("player your money is", self.MoneyP6)
          self.withbet12 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player12 = 0
          self.withbet12 = 1

    if  self.numPlayer >= 13 and self.player13 == 1 and self.withbet13 != 1:
      print("\nplayer 13 your cards are", self.player13hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP13 -= self.betAmount
          print("player your money is", self.MoneyP13)
          self.withbet13 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player13 = 0
          self.withbet13 = 1\

    if  self.numPlayer >= 14 and self.player14 == 1 and self.withbet14 != 1:
      print("\nplayer 14 your cards are", self.player14hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP14 -= self.betAmount
          print("player your money is", self.MoneyP14)
          self.withbet14 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player14 = 0
          self.withbet14 = 1

    if  self.numPlayer >= 15 and self.player6 == 15 and self.withbet15 != 1:
      print("\nplayer 15 your cards are", self.player15hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP15 -= self.betAmount
          print("player your money is", self.MoneyP15)
          self.withbet15 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player15 = 0
          self.withbet15 = 1

    if  self.numPlayer >= 16 and self.player16 == 1 and self.withbet16 != 1:
      print("\nplayer 16 your cards are", self.player16hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP16 -= self.betAmount
          print("player your money is", self.MoneyP16)
          self.withbet16 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player16 = 0
          self.withbet16 = 1

    if  self.numPlayer >= 17 and self.player17 == 1 and self.withbet17 != 1:
      print("\nplayer 17 your cards are", self.player17hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP17 -= self.betAmount
          print("player your money is", self.MoneyP17)
          self.withbet17 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player17 = 0
          self.withbet17 = 1

    if  self.numPlayer >= 18 and self.player18 == 1 and self.withbet18 != 1:
      print("\nplayer 18 your cards are", self.player18hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP18 -= self.betAmount
          print("player your money is", self.MoneyP18)
          self.withbet18 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player18 = 0
          self.withbet18 = 1

    if  self.numPlayer >= 19 and self.player19 == 1 and self.withbet19 != 1:
      print("\nplayer 19 your cards are", self.player19hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP19 -= self.betAmount
          print("player your money is", self.MoneyP19)
          self.withbet19 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player19 = 0
          self.withbet19 = 1

    if  self.numPlayer >= 20 and self.player20 == 1 and self.withbet20 != 1:
      print("\nplayer 20 your cards are", self.player20hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP20 -= self.betAmount
          print("player your money is", self.MoneyP20)
          self.withbet20 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player20 = 0
          self.withbet20 = 1

    if  self.numPlayer >= 21 and self.player21 == 1 and self.withbet21 != 1:
      print("\nplayer 21 your cards are", self.player21hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP21 -= self.betAmount
          print("player your money is", self.MoneyP21)
          self.withbet21 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player21 = 0
          self.withbet21 = 1

    if  self.numPlayer >= 22 and self.player22 == 1 and self.withbet22 != 1:
      print("\nplayer 22 your cards are", self.player22hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP22 -= self.betAmount
          print("player your money is", self.MoneyP22)
          self.withbet22 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player22 = 0
          self.withbet22 = 1

    if  self.numPlayer >= 1 and self.player1 == 1 and self.withbet1 != 1:
      print("\nplayer 1 your cards are", self.player1hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP1 -= self.betAmount
          print("player your money is", self.MoneyP1)
          self.withbet1 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player1 = 0
          self.withbet1 = 1

    if  self.numPlayer >= 2 and self.player2 == 1 and self.withbet2 != 1:
      print("\nplayer 2 your cards are", self.player2hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP2 -= self.betAmount
          print("player your money is", self.MoneyP2)
          self.withbet2 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player2 = 0
          self.withbet2 = 1

    if  self.numPlayer >= 3 and self.player3 == 1 and self.withbet3 != 1:
      print("\nplayer 3 your cards are", self.player3hand)
      self.pChoice = input("would you like to call or fold?: ")
      if self.pChoice == "call":
          print("player has called")
          self.MoneyP3 -= self.betAmount
          print("player your money is", self.MoneyP3)
          self.withbet3 = 1
      if self.pChoice == "fold":
          print("player has folded")
          self.player3 = 0
          self.withbet3 = 1
  def endGame(self):
    print("remaining player will now show ther cards")
    if  self.numPlayer >= 4 and self.player4 == 1:
      print("player 4 has", self.player4hand)
    if  self.numPlayer >= 5 and self.player5 == 1:
      print("player 5 has", self.player5hand)
    if  self.numPlayer >= 6 and self.player6 == 1:
      print("player 6 has", self.player6hand)
    if  self.numPlayer >= 7 and self.player7 == 1:
      print("player 7 has", self.player7hand)
    if  self.numPlayer >= 8 and self.player8 == 1:
      print("player 8 has", self.player8hand)
    if  self.numPlayer >= 9 and self.player9 == 1:
      print("player 9 has", self.player9hand)
    if  self.numPlayer >= 10 and self.player10 == 1:
      print("player 10 has", self.player10hand)
    if  self.numPlayer >= 11 and self.player11 == 1:
      print("player 11 has", self.player11hand)
    if  self.numPlayer >= 12 and self.player12 == 1:
      print("player 12 has", self.player12hand)
    if  self.numPlayer >= 13 and self.player13 == 1:
      print("player 13 has", self.player13hand)
    if  self.numPlayer >= 14 and self.player14 == 1:
      print("player 14 has", self.player14hand)
    if  self.numPlayer >= 15 and self.player15 == 1:
      print("player 15 has", self.player15hand)
    if  self.numPlayer >= 16 and self.player16 == 1:
      print("player 16 has", self.player16hand)
    if  self.numPlayer >= 17 and self.player17 == 1:
      print("player 17 has", self.player17hand)
    if  self.numPlayer >= 18 and self.player18 == 1:
      print("player 18 has", self.player18hand)
    if  self.numPlayer >= 19 and self.player19 == 1:
      print("player 19 has", self.player19hand)
    if  self.numPlayer >= 20 and self.player20 == 1:
      print("player 20 has", self.playe206hand)
    if  self.numPlayer >= 21 and self.player21 == 1:
      print("player 21 has", self.player21hand)
    if  self.numPlayer >= 22 and self.player22 == 1:
      print("player 22 has", self.player22hand)
    if  self.numPlayer >= 1 and self.player1 == 1:
      print("player 1 has", self.player1hand)
    if  self.numPlayer >= 2 and self.player2 == 1:
      print("player 2 has", self.player2hand)
    if  self.numPlayer >= 3 and self.player3 == 1:
      print("player 3 has", self.player3hand)
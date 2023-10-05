#Wesley, Paul, Jude, Andy, jayden
from players import cards
class main ():
    def __init__(self):
        self.cards = cards
    def dealCards(self):
        return self.deal
    def flopCards (self):
        return self.flop
    def turnCards (self):
        return self.turn
    def riverCards (self):
        return self.river 
    def foldCards (self):
        answer = eval(input("Would you like to fold ?(Yes:1 No:0): "))
        if answer == 1 :
         print("Your done for the round")
        else :
            print("Continoue on")
    def veiwCards (self):
        print(" When its your players turn to veiw there cards click enter ")
        print("After you click enter , click enter again and hand the computer to the next player so they can view theyre cards")

    def showCards (self):
        print(cards)

    def allIn(self):
        print("Are you sure you want to go all in ? Y or N")
        if ("Y"):
            print("You are all in")
            
        else:
            print("You have decided to change your move.")
            
    def foldCards(self):
        self.fold = print()
        return self.fold

  

    
    

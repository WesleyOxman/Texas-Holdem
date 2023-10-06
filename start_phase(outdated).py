#(put name here)
class Start_Phase:
    def __init__(self):
        self.starting_funds = 100
        self.big_flop = players[0]
        self.lil_flop = players[1]
        self.starting_bet = 5
        self.full_round = 0
  #makes small and big flop
    def setUpBig(self):
        self.big_flop = players[0]
        players.append(players[0])
        del players[0]
    def setUpSmall(self):
        self.lilflop = players[0]
        players.append(players[0])
        del players[0]


    def starting_bet(self):
        if self.full_round > numPlayer:
            self.starting_bet += 5
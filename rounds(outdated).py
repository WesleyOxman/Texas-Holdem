import random
from players import numPlayers
#Start new round
def start_round():
    #Deal two cards to each player
    players = numPlayers
    for _ in range(2):
        for player in players:
            card = deck.pop()
            players[player].append(card)

#End round
def end_round():
    #collect and shuffle the used cards back into the deck
    deck.extend(players.values())
    random.shuffle(deck)

    #Clear players hands for the next round
    for player in players:
        players[player] = []

#Main game loop
players = numPlayers

while True:
    start_round()

    end_round() 

    play_again = input("Do you want to play another round? (yes/no): ")

    if play_again.lower() != "yes":
        break   
print("Game over!")
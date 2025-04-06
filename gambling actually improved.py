"""
Upto 10 players can play this game
for upto 10 rounds.
No of rounds can be decided.
Each player has a name and a score.
Player has a score of 0 at the start.
Roll a die and the result is added to the score.
Rolling a 1 will reset the score to 0.
You can cancel in the middle of the game to avoid a 1 and save your score.
1 round is completed when all players have rolled the die.
The next round starts and the above is repeated until the no of rounds is completed.
Scores of a player from all rounds are added to the final score.
"""

import random

player = [None] # list of player instances (1 indexed)
rounds = 0 # global variable for number of rounds
r = 0 # global variable for current round
players = 0 # global variable to keep track of number of players

class Player:
    def __init__(self, name):
        self.name = name
        self.finalScore = 0
        self.scoreInRound = [None] + [0 for i in range(rounds)] # 1 indexed
        player.append(self)

def shuffle(player: list):
    players = len(player) # number of players
    playerT = player[1:]  # temporary list of players (0th index will be None)
    random.shuffle(playerT) # shuffle the players
    player = [None]+playerT # Thank you NCR

def playTurnOf(p: Player):
    assert rounds in range(1,11) , "Rounds should be between 1 and 10"

    while True:
        global r
        global player
        global players

        choice = input("Do you want to roll? y or n: ")
        if choice.lower() == 'y':
            throw = random.randint(1,6)
            # score update or elimination after throw
            if throw != 1: p.scoreInRound[r] += throw
            else: print(f"{p.name} was eliminated after rolling a 1"); return

        elif choice.lower() == 'n':
            return
        else:
            print("Please enter a valid choice")

def start():
    global r
    global rounds

    for i in range(1,rounds+1):
        r+=1
        for p in player[1:]:
            playTurnOf(p)

rounds = int(input("Enter number of rounds: "))
assert rounds in range(1,11), "Rounds should be between 1 and 10"

players = int(input("Enter number of players: "))

for i in range(1,players+1):
    player.append(Player(input(f"Enter name of player {i}: ")))

shuffle(player)
print([p.name for p in player[1:]]) # print names of players
start()

for p in player[1:]:
    p.finalScore = sum(p.scoreInRound[1:])

for p in player[1:]:
    print(f"{p.name} scored {p.finalScore} in total")
    print()
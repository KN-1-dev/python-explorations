"""
Upto 10 players can play this game.
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

class Player:
    def __init__(self, name):
        self.name = name
        self.finalScore = 0
        self.scoreInRound = [0 for i in range(globals().get('rounds'))]
        player.append(self)

def startGame(player: list, rounds: int):
    players = len(player) # number of players
    player
    random.shuffle(player[1:]) # shuffle the players
    for r in range(1,rounds+1):
        for p in range(1,players+1):
            

# 
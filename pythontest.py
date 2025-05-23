# The compiler should ask for number of players
# Ask whether the player wants to roll the die or not 
# Generate a random number between 1 to 6
# if the number is between 2 to 6 , add it to the current player's score
# if the number is 1 then the player is eliminated
# or if the player enters 'n' then stop the current player's turn and display the score and go to the next player
# display the player's score and go to the next player 
# if the player enters the letter 'y' or 'n' and then types anything else dont consider it and ask him to enter again , same is he doesn't enter either 'y' or 'n' -->extra feature
# After all the players are done display the scores of all the players and state the player who won --> extra feature
# Input the names of the players:
# Display the current score of the player after every roll
# Make it unbeatable for particular cases
import random

def gameTime():
    roll = random.randint(1,6)
    return roll
pagain = ''
count  = 0
nplayers = 0
d = {}
pchoice = ''
score = 0
pcount = 0
pnames = []
pname  = ''
# Outer loop if the players want to play another round
while True:
    while True:
        # Taking in the number of players
        print("Enter the number of players: ")
        nplayers = int(input())
        for i in range(nplayers):
            print(f'Enter player {i} name : ', end = '')
            pname = input()
            pnames.append(pname)
            d[pnames[i]] = 0
        break
    for _ in range(nplayers):
        # below is for a single player's turn
        while True:
            print("Do you want to roll? y or n ") # Asking for roll
            pchoice = input()
            if pchoice not in ['y','n']: # Checking for invalid input
                print("Please enter a valid choice")
                continue
            if pchoice == 'y': # If the player rolls 
                score = gameTime()
                if score == 1: # If 1 is rolled the player is eliminated
                    score = 0
                    d[pnames[pcount]] = 0 # His score becomes zero
                    print("You rolled a 1 -> Eliminated")
                    print(f'Your score is : {d[pnames[pcount]]}')
                    pcount += 1 # Going to the next player
                    break
                else:
                    print(f'You rolled a {score}')
                    d[pnames[pcount]]+= score 
                    print(f'Your current score : {d[pnames[pcount]]}')
            
            elif pchoice == 'n': # if the player wants to stop
                score = 0 # setting the score back to zero for next player
                print(f"Turn ended, {pnames[pcount]} scored : {d[pnames[pcount]]}")
                pcount+=1
                if pcount< len(pnames):
                    print(f'Please pass to {pnames[pcount]}')
                break
    max_score = max(d.values()) # Once the round is finished finding the max score
    for i in range(nplayers):
        print(f'The player {pnames[i]} scored {d[pnames[i]]}') # Displaying the player's scores along with the winner
        if d[pnames[i]] == max_score:
             print(f'The player {pnames[i]} has the max score : {d[pnames[i]]},  is the Winner!!')
             print()
    count += 1 # Keeps track of the rounds
    pcount = 0 # setting player count to zero for next round
    if count != 0:
        print("Do you want to play again? ")
        pchoice = input()
        if pchoice == 'n': # if n is entered the game ends
            print("The game has ended :)")
            break




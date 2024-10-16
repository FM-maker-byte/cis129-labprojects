# Lab 7-3 The Dice Game 
# Faith Moses
# 10/22/2024
# Add libraries needed, write dice game in python code
import random 

# The main function 
def main(): 
    print
    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo) 

    # while loop to run program again 
    while endProgram == 'no': 

        # populate variables 
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)
        
        # call to displayInfo 
        displayInfo(winnerName)
    
        endProgram = input('Do you want to end program? (yes/no): ') 

# This function gets the players names 
def inputNames(playerOne, playerTwo):
    playerOne = input('Please enter player 1 name: ')
    playerTwo = input('Please enter player 2 name: ')
    return playerOne, playerTwo

# This function will get the random values 
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6) 
    p2number = random.randint(1, 6) 
    if p1number == p2number:
        winnerName = 'TIE'
    elif p1number > p2number:
        winnerName = playerOne
    else:
        winnerName = playerTwo
    return winnerName

# This function displays the winner 
def displayInfo(winnerName):
    print('The winner is', winnerName)

# calls main 
main()

# Lab 6 Hotdog Cookout Lab
# Faith Moses
# 10/14/2024
# The required and leftover amounts of hotdogs and the hotdog buns in a cookout.

# Main function
def main():
    totalHotDogs = 0
    totalHotDogs = getTotalHotDogs() # call to get total hot dogs
    hotDogResults = showResults(totalHotDogs) # call to show results

# This function gets total hotdogs
def getTotalHotDogs():
    attendees = 0 
    hotDogs = 0
    attendees = int(input('Enter the number of attendees: '))
    hotDogs = int(input('Hot dogs per attendee: '))
    totalHotDogs = attendees * hotDogs
    return totalHotDogs 

# This function calculates the required and leftover amounts of hotdogs and hotdog buns.
def showResults(totalHotDogs):
    DOGS = 10
    BUNS = 8
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0
    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS 
    minDogs = int(totalHotDogs / DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS
    minBuns = int(totalHotDogs / BUNS) + (0 ** (0 ** bunsLeft))
    
# This section prints the hotdog and hotdog bun amounts found in the prior calculations. 
    print('Minimum packages of hotdogs needed: ', minDogs)
    print('Minimum packages of hotdog buns needed: ', minBuns)
    print('Hotdogs Remaining: ', dogsLeft)
    print('Hot dog buns remaining: ',bunsLeft)

# call to main
main()

# Lab 5 The Bottle Return Program
#Faith Moses
# 10/07/2024
# Program counts the number of bottles in a week and applies a total payout. 

#main function
def main():
    #declare local variables
    # totalBottles = 0
    # counter = 1
    # todayBottles = 0
    # real totalPayout  

    keepGoing = 'y'
    while keepGoing == 'y':    #repeats as long as another week of data is added
        totalBottles = getBottles()    # call to getBottles
        totalPayout = calcPayout(totalBottles) #call to calcPayout
        printInfo(totalBottles, totalPayout) # call to printInfo
        print("Do you want to enter another week's worth of data?")
        keepGoing = input("Enter y or n:")
 
#This function gets the total bottles
#nmb_of_days = 7
def getBottles():
    totalBottles = 0
    counter = 1
    todayBottles = 0

    while counter <= 7:  #repeats counting bottles up to 7 days 
        print("Enter number of bottles returned for day #",
              counter, ":")
        todayBottles = int(input())
        totalBottles = totalBottles + todayBottles 
        counter = counter + 1
    else: 
        return totalBottles       
       
#This function gets the total payout
def calcPayout(totalBottles):
    payoutPerBottle = 0.10 
    totalPayout = 0 
    totalPayout = totalBottles * payoutPerBottle 
    return totalPayout

#This function prints the total bottles and total payout
def printInfo(totalBottles, totalPayout):
    print('The total number of bottles collected is', totalBottles)
    print (f'The total paid out is $ {totalPayout:.2f}')

#calls main
main()

# Module 4 Lab 4
# Faith Moses
# 9/25/2024
# Retail company store and employee bonus- program example

#The Main Function
def main(): 
    #declare local variables
    # monthlySales = monthly sales amount
    # storeAmount = store bonus amount
    # empAmount =  employee bonus amount
    # SalesIncrease = percent of sales increase
    monthlySales = getSales()
    salesIncrease = getIncrease()
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales(): 
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease(): 
    salesIncrease = float(input('Enter percent of sales increase: '))
    salesIncrease = salesIncrease / 100
    return salesIncrease # This function determines the storeAmount bonus

def calcStoreBonus(monthlySales): 
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else: 
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease): 
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

#This function prints the bonus information 
def printBonus(storeAmount, empAmount): 
    print('The store bonus amount is $', storeAmount)
    print('The employee bonus amount is $', empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus',
          'amounts possible!')\

# calls main 
main () 

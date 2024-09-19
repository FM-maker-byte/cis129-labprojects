#Receipt Coding Practice
#CIS129
#Creator: Faith Moses

#Getting input
print('What are you purchasing?')
nameOfItem = input('Name of Item 1')
nameOfItem_2 = input('Name of Item 2')
print('Please enter the number of items bought')
numberOfItemsPurchased = int(input('Number of Coffees Purchased'))
numberOfItemsPurchased_2 = int(input('Number of Muffins Purchased'))
print('Please enter the price of the item')
priceOfItem = int(input('Price of Coffee'))
priceOfItem_2 = int(input('Price of Muffin'))
coffeeTotalCost = numberOfItemsPurchased * priceOfItem
muffinTotalCost = numberOfItemsPurchased_2 * priceOfItem_2
taxOfTotal = (coffeeTotalCost + muffinTotalCost) * 0.06
#Display Receipt to Customer
print('***************************************************')
print('        My Coffee and Muffin Shop')
print('Number of Coffees bought?', numberOfItemsPurchased)
print('Number of Muffins bought?', numberOfItemsPurchased_2)
print('*****************************************************')
print('*****************************************************')
print('My Coffee and Muffin Shop Receipt')
print('1 Coffee at $5 each:         $', coffeeTotalCost)
print('2 Muffins at $4 each:        $', muffinTotalCost)
print('6% tax:                      $', taxOfTotal)
print('                           ----------------------')
print('Total:                       $', (coffeeTotalCost + muffinTotalCost 
                                         + taxOfTotal))
print('*****************************************************')

#Further customization can be done for the receipt, including the price and layout. 

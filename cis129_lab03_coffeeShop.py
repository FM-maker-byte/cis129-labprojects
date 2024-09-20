#Receipt Coding Practice
#CIS129
#Creator: Faith Moses

# What are you purchasing
nameOfItem = 'Coffees'
nameOfItem_2 = 'Muffins'
nameOfItem_3 = 'Tea'
nameOfItem_4 = 'Bagels'

#Getting Input

print('Please enter the number of items bought')
numberOfItemsPurchased = int(input('Number of Coffees Purchased'))
numberOfItemsPurchased_2 = int(input('Number of Muffins Purchased'))
numberOfItemsPurchased_3 = int(input('Number of Tea Purchased'))
numberOfItemsPurchased_4 = int(input('Number of Bagels Purchased'))

print('Please enter the price of the item')
priceOfItem = int(input('Price of Coffee'))
priceOfItem_2 = int(input('Price of Muffins'))
priceOfItem_3 = int(input('Price of Tea'))
priceOfItem_4 = int(input('Price of Bagels'))

coffeeTotalCost = numberOfItemsPurchased * priceOfItem
muffinTotalCost = numberOfItemsPurchased_2 * priceOfItem_2
teaTotalCost = numberOfItemsPurchased_3 * priceOfItem_3
bagelTotalCost = numberOfItemsPurchased_4 * priceOfItem_4


taxOfTotal = (coffeeTotalCost + muffinTotalCost
               + teaTotalCost +bagelTotalCost) * 0.06

#Display Receipt to Customer
print('***************************************************')
print('        My Breakfast Shop')
print('Number of coffees bought?', numberOfItemsPurchased)
print('Number of Muffins bought?', numberOfItemsPurchased_2)
print('Number of Teas bought?', numberOfItemsPurchased_3)
print('Number of Bagels bought?', numberOfItemsPurchased_4)


print('*****************************************************')
print('*****************************************************')
print('My Breakfast Shop Receipt')
print(numberOfItemsPurchased, nameOfItem, 'at',
      priceOfItem, 'each:         $', coffeeTotalCost)
print(numberOfItemsPurchased_2, nameOfItem_2, 'at',
      priceOfItem_2, 'each:         $', muffinTotalCost)
print(numberOfItemsPurchased_3, nameOfItem_3, 'at',
      priceOfItem_3, 'each:             $', teaTotalCost)
print(numberOfItemsPurchased_4, nameOfItem_4, 'at',
      priceOfItem_4, 'each:          $', bagelTotalCost)


print('6% tax:                      $', taxOfTotal)
print('                           ----------------------')
print('Total:                     $', (coffeeTotalCost + muffinTotalCost 
                                       + teaTotalCost + bagelTotalCost 
                                       + taxOfTotal))
print('Thank you for shopping at our Breakfast Shop!',
      'Have a Wonderful day!')
print('*****************************************************') 

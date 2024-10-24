# Lab 8 Palindrome 
# Faith Moses
# 10/22/24 
# Program tests a Palindrome that is inputted, with an (optional) loop to go again

# Local Variables
# testPal = is_palindrome(p)  # Call to test if the word is a palindrome
# palResult = inputTest(testPal) # Call to get palindrome results
# printInfo(palResult) # Call to print true or false verdict

# Function to test if it is a palindrome or not 
def is_palindrome(p):
    stack = []        
    for letter in p:
        stack.append(letter)
    for letter in p:
        if letter != stack.pop():
            return False 
    return True

   # Input function for Palindrome test
def inputTest(testPal):
    p = input('Insert your word to test if it is a palindrome: ')
    palResult = is_palindrome(p.casefold())
    return palResult         

# Print true or false 
def printInfo(palResult):
    print(palResult) 

# Loop to do another test
contProgram = 'yes'
while contProgram == 'yes':
    p = 'none'
    testPal = is_palindrome(p.casefold())
    palResult = inputTest(testPal)
    printInfo(palResult)
    contProgram = input('Do you want to test another palindrome? (yes/no) ').casefold()

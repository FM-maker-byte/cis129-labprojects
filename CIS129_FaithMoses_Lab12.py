# Module 12 Lab Create a Class Pet
# CIS129
# Faith Moses
# 12/02/2024

# Create a class called newPet 
class newPet:
    # Initialization Constructor
    def __init__(self):
        self.name = None
        self.type = None
        self.age = None

    # Mutators (set)
    def setName(self, n):
        self.name = n
    def setType(self, t):
        self.type = t
    def setAge(self, a):
        self.age = a
    
    # Accessors (get)
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age





 # Main module
def main():
    # Declare input variables
    # name = inputName()
    # type = inputType()
    # age = inputAge()
    # Create a new pet object
    Animal = newPet()

	# Get input values then calling methods and passing their respective arguements
    inputName = input("Enter the pet name: ")
    Animal.setName(inputName)
    inputType = input("Enter the pet type: ")
    Animal.setType(inputType)
    inputAge = int(input("Enter the pet age: "))
    Animal.setAge(inputAge)
    
    # Show values for this pet
    print('----------------------------------')   # separate input values and the output
    print("The pet name is" , Animal.getName()) 
    print("The pet type is" , Animal.getType())
    print("The pet age is" , str(Animal.getAge()))

if __name__ == '__main__':
    main()
        

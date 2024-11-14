# Module 11 9.1 and 9.2 Class Average Lab
# CIS 129
# Faith Moses
# 11/18/2024

# The section to write a new grades.txt file (9.1)

fileGrade = 'grades.txt'
with open(fileGrade, mode='w') as file:      # writes a new grades.txt file
    while True:                              # loops the process of grade input until -1
        grade = int(input('Enter grade, -1 to end: '))
        if grade != -1: 
            file.write(f'{grade}\n')
        else: 
            break

    

# The section to read a grades.txt file and display the grades (9.2)
with open('grades.txt', mode='r') as values:       # opens the grades.txt file to read
    total = 0 
    grades = values.readlines()                 # reads the grade values in the text
    print('--------------------\n')             # Easier readabilty for the write and read sections
    print(f'{"Grade":<10}')                     # prints grade title
    for grade in grades:                        # iterates through grades and prints                       
        grade = int(grade.strip())
        print(f'{grade:<10}')
        

# The section to calculate the total, count, and average of grades 
        total += int(grade)
        count = len(grades)
        average = total/len(grades)


# The section to print the total, count, and average
print(f'{"Total":<10}{"Count":<10}{"Average":>10}')
print(f'{total:<10}{count:<10}{average:>10.2f}')

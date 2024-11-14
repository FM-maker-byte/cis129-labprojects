# Module 11 9.3 Class Average Lab
# CIS 129
# Faith Moses
# 11/18/2024

import csv                 # importing csv module from python library


# Function to get the student input data
def getStudentData():
    firstName = input("Enter student's first name: ")
    lastName =  input("Enter student's last name: ")
    exam1Grade = int(input('Exam 1 grade: '))
    exam2Grade = int(input ('Exam 2 grade: '))
    exam3Grade = int(input('Exam 3 grade: '))
    studentData = [firstName, lastName, exam1Grade, exam2Grade, exam3Grade]
    return studentData


# Function to write a CSV grade file
def write_grade_CSV(fileGrade, studentData):  # writing a new csv file for student data
        writer = csv.writer(file)                        
        writer.writerow(studentData)



# The section to loop student data input while yes
fileGrade = 'grades.csv'
with open(fileGrade, mode='w', newline='') as file:   # opening a new csv file for student data
    while True:                                          
         studentData = getStudentData()
         write_grade_CSV(fileGrade, studentData)
         repeat = input("Do you want to add another student's info? (yes/no): ")
         if repeat.casefold() != 'yes':
              break
         else:
              True
        

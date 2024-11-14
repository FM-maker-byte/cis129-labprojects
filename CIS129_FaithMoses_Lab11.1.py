# Module 11 9.3 Class Average Lab
# CIS 129
# Faith Moses
# 11/18/2024

import csv                 # importing csv module from python library

def getStudentData():      # function to get the student data input
    firstName = input("Enter student's first name: ")
    lastName =  input("Enter student's last name: ")
    exam1Grade = input('Exam 1 grade: ')
    exam2Grade = input ('Exam 2 grade: ')
    exam3Grade = input('Exam 3 grade: ')
    studentData = [firstName, lastName, exam1Grade, exam2Grade, exam3Grade]
    return studentData

def write_grades_CSV(studentData):     # function to write csv grade file using student data input
    fileGrade = 'grades.csv'
    with open(fileGrade, mode='w', newline='') as file:      # writing a new csv file for student data
        while True:                                          # looping student data input while yes
            getStudentData()
            repeat = input("Do you want to add another student's info? (yes/no): ")
            if repeat.casefold() == 'yes':
                writer = csv.writer(file)
                writer.writerow(studentData)
            else: 
                break

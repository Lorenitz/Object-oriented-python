# main student property example

from Student import *

oStudent1 = Student('Joe Smicht')
oStudent2 = Student('Jane Smidth')

# Get the student's grade using the grade property and print
print(oStudent1.grade)
print(oStudent2.grade)
print()

# Set new value using the 'grade' property

oStudent1.grade = 85
oStudent2.grade = 95

print(oStudent1.grade)
print(oStudent2.grade)
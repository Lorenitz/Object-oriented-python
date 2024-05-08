# Person example main program using getter and setters

from Person import *

oPerson1 = Person('Joe Schmore', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the salaries using getter and print
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Set the salaries using setter
oPerson1.setSalary(100000)
oPerson2.setSalary(110000)

# Get the salaries and print again
print(oPerson1.getSalary())
print(oPerson2.getSalary())
# Employee Manager Inheritance

# Define the employee class, which we will use as a base class

class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour
        
    def getName(self):
        return self.name
    
    def getTitle(self):
        return self.title 
    
    def payPerYear(self):
        # 52 weeks * 5 days a week * 8 hours per day
        
        pay = 52 * 5 * 8 * self.ratePerHour
        
        return pay
    
# Define a manager subclass that inherits from Employee

class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        
        super().__init__(name, title)
    
    def getReports(self):
        return self.reportsList 
    
    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
           pay = pay + (.10 * self.salary) # add a bonus of 10% 
           print(self.name, 'gets a bonus for good work')
        return pay      
    
    
# Create objects

oEmployee1 = Employee('Joe Schoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)

oManager = Manager('Sue', 'Pizza restaurant manager', 55000, [oEmployee1, oEmployee2])

# Call methods of the employee objects

print('Employee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))

print('Employee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))

# Call methods of the Manager object

managerName = oManager.getName()
print('Manager name:', managerName)

# Give the manager a bonus

print('Manager Salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')

reportsList = oManager.getReports()

for oEmployee in reportsList:
    print(' ', oEmployee.getName(), '(' + oEmployee.getTitle() + ')')
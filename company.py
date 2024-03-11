#This code defines several classes (company, employee, salaryemployee, hourlyemployee, commissionemployee) and a main function.

from employee import employee, salaryemployee, hourlyemployee, commissionemployee;

class company:
    def __init__(self): #self is always needed when defining a class
        self.employees = [];

    def addemployee(self, newemployee):
        self.employees.append(newemployee);

    def displayemployees(self):
        print('current employees')
        for i in self.employees:
            print(i.fname, i.lname)
        print('---------')
    
    def payemployees(self):
        print('paying employees:')
        for i in self.employees:
            print(f'Amount: ${i.calculatepaycheck():,.2f}'); #:,.2fformats a number with two decimal places and includes commas as thousands separators, i formats as currency

def main ():
    mycompany = company()

    employee1 = salaryemployee('jan','smith',100000)
    mycompany.addemployee(employee1)
    employee2 = hourlyemployee('jack','stan',25, 50)
    mycompany.addemployee(employee2)
    employee3 = commissionemployee('jane','doe', 30000, 5, 200)
    mycompany.addemployee(employee3)

    mycompany.displayemployees();
    mycompany.payemployees();

main();

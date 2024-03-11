#This code defines a hierarchy of employee classes for different types of compensation structures: salary-based, hourly-based, and commission-based. 

class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname 


class salaryemployee(employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculatepaycheck(self):
        return self.salary/52
    
class hourlyemployee(employee):
    def __init__(self, fname, lname, weeklyhours, hourlyrate):
        super().__init__(fname, lname)
        self.weeklyhours = weeklyhours
        self.hourlyrate = hourlyrate

    def calculatepaycheck(self):
        return self.weeklyhours*self.hourlyrate;
    
class commissionemployee(salaryemployee):
    def __init__(self, fname, lname, salary, salesnum, comrate):
        super().__init__(fname, lname, salary)
        self.salesnum = salesnum;
        self.comrate = comrate;

    def calculatepaycheck(self):
        regularsalary = super().calculatepaycheck()
        totalcommission = self.salesnum*self.comrate;
        return regularsalary+totalcommission;

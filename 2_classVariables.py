class Employee:
    
    auto_inc=1.04
    no_of_emp=0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname=lname
        self.pay=pay
        self.email = fname + '.' + lname + '@company.com'

        Employee.no_of_emp+=1
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def payInc(self):
        self.pay=int(self.pay*self.auto_inc)


emp1 = Employee('Shubham','Masang',100)
emp2 = Employee('Lalit','Girase',50)

# print(emp1.pay)
# emp1.payInc()
# print(emp1.pay)

print(Employee.no_of_emp)


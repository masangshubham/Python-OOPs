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

    @classmethod
    def set_raise(cls,amt):
        cls.auto_inc=amt

    @classmethod
    def fromString(cls,str):
        first , last, pay = str.split('-')
        return cls(first, last, pay)
    


emp1 = Employee('Shubham','Masang',100)
emp2 = Employee('Lalit','Girase',50)

emp_str='Parth-Virdhe-20'

# first , last, pay = emp_str.split('-')
# new_emp=Employee(first, last, pay)
new_emp=Employee.fromString(emp_str)

print(new_emp.email)
print(new_emp.pay)

# print(emp1.auto_inc)
# print(Employee.auto_inc)
# print(emp2.auto_inc)

# Employee.set_raise(1.05)

# print(emp1.auto_inc)
# print(Employee.auto_inc)
# print(emp2.auto_inc)

class Employee:
    # __init__ method in python is for initialization
    # basically a constructor
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname=lname
        self.pay=pay
        self.email = fname + '.' + lname + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)



emp1 = Employee('Shubham','Masang',100)
emp2 = Employee('Lalit','Girase',50)

print(emp1.fullname())
print(emp2.fullname())

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

#For Inheritance pass the parent class in () to child class
#when we create a child all parent attributes and methods are carried on to child.
class Developer(Employee):
    auto_inc=1.10

    def __init__(self, fname, lname, pay, p_lang):
        super().__init__(fname, lname, pay)
        self.p_lang=p_lang


dev1 = Developer('Shubham','Masang',100,'CPP')
emp2 = Employee('Lalit','Girase',50)

# print(dev1.fullname())
# print(dev1.p_lang)

print(dev1.pay)
dev1.payInc()
print(dev1.pay)


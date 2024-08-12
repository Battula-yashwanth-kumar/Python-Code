class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

class detils(Employee):
    def __init__(self,name, salary, address, pincode):
        super().__init__(name,salary)
        self.address=address
        self.pincode=pincode
       

hello=detils("ckwlck","cwlcklq","cexjoko","dkfqoiow")
print(hello.name)

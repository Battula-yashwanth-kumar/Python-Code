class Employee :
    no_of_leaves=8
    def __init__(self,aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    
    @staticmethod
    def printgood(string):
        print("cmalkclakw"+string)

hello=Employee("wclkwlckl",56656,"ackalck")
# Employee.change_leaves(35)
# hello.change_leaves(62)
# print(hello.no_of_leaves)
# print(Employee.no_of_leaves)
print("Hello",Employee.printgood("wcmkwel"))
print(hello.printgood("kqjdlqfjkwq"))
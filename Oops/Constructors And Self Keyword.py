#self keyword is used in the method to refer the instance of the curretn class we are using
#the self keyword is passed as a parameter explicitly every time we define a method
#__int__ is also called a constructor in object oriented terminology

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

hello=Employee("wclkwlckl",56656,"ackalck")
Employee.change_leaves(35)
hello.change_leaves(62)
print(hello.no_of_leaves)
print(Employee.no_of_leaves) #as we are using function to change the no of leaves in the class where leaves variable is defined , it will change the all over the class and instances
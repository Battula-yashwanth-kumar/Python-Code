# Dunder Methods in python are developed are special methods. In python we sometimes see methods names with a double underscore(__), such as the __init__ method that every class has. These methods are called magic or dunder methods.




class Employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}str"
    def __repr__(self):
        return f"Employeed('{self.name}')"
    def __call__(self):
        print("Hy good morning")

e=Employee("kcwckl")
print(e.name)
print(len(e))  
print(str(e))  #str method is mainly written for end users
print(repr(e)) #repr method is mainly written for developer
e() # call method  will be called

        
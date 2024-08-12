class Employee:
    no_of_leaves=5
    def __init__(self, salary, name,role):
        self.salary=salary
        self.name=name
        self.role=role
    
    @classmethod
    def function(cls,string):
        # params=string.split('-')
        # print(params)
        # return cls(params[0],params[1],params[2])

        # these  above commented line can be replaced by a single line

        return cls(*string.split('-'))

hello=Employee.function("ckcjkw-ckejvkw-vkwkl")
print(hello.salary,hello.name)
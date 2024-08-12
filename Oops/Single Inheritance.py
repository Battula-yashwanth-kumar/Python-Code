class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


class programmer(Employee):
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def printgo(cls, string):
        print(string)


hello = Employee("wclkwlckl", 56656, "ackalck")
world = programmer("dsckk", 522, "ewkdweofko")
# Employee.change_leaves(35)
# hello.change_leaves(62)
# print(hello.no_of_leaves)
# print(Employee.no_of_leaves)
print(world.printdetails())

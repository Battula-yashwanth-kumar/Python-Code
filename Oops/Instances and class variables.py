class Employee :
    no_of_leaves=5
    pass
hello=Employee()
world=Employee()
hello.name="acklck;q"
hello.salary=5685
hello.role="instructor"
world.name=",smcskcl"
world.role="acalckla"
world.no_of_leaves=52 #these will not change the actual value of no of leaves instead it create a copy of for this "world" instance 
print(world.no_of_leaves)
print(hello.no_of_leaves)
print(hello.__dict__)
print(world.__dict__)


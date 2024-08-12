class Employee:
    var = 2
    _protec = 9  # _ for protected variable
    __privat = 98  # __ for private variable

emp = Employee()
print(emp._protec)  # Accessing the protected variable
print(emp._Employee__privat)  # Accessing the private variable using name mangling

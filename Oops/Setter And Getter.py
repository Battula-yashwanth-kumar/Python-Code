class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
    def details(self):
        return f"{self.name} and {self.lastname}"
    
    @property  # for getter method
    def email(self):
        if self.name is None or self.lastname is None:
            return "Email is not set. Please set it using the setter."
        else:
            return f"{self.name}.{self.lastname}@gmail.com"
    
    @email.setter  # Setter method
    def email(self, string):
        names = string.split('@')[0]  # Get the part before '@'
        self.name = names.split('.')[0]
        self.lastname = names.split('.')[1]
    
    @email.deleter
    def email(self):
        self.name = None
        self.lastname = None

hello = Employee("John", "Doe")
print(hello.details())
print(hello.email)

hello.email = "new.firstname.lastname@gmail.com"
print(hello.details())
print(hello.email)

del hello.email
print(hello.details())
print(hello.email)

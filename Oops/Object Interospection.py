# Introspection can be said as the ability to recognize the object along with all its details, such as id or location at runtime
# one of the most basic introspection we came across many times earlier is type() & id() & dir()
# hasattr() --> It checks if an object has an attribute
# similarly, getattr(),repr(),vars(),issubclass(),isinstance(),__doc__, __name__, callable(),help()

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

hello=Employee("kcjlcksa","wkevlkwe;")
print(hello.email)
print(dir(hello))
print(id("fmewm,ec"))
import inspect
print(inspect.getmembers(hello))
print(hasattr(hello,'name'))
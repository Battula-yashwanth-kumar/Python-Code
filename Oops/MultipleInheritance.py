
class Employee:
    var=10;
    def __init__(self, name):
     self.name=name
    def printgood(self,string):
       return f"cmkccmkw {self.name} {string}"
class programmer:
   var=15
   def __init__(self,name):
      self.name=name;

class multi(programmer,Employee):
   
   vari=10
   pass

hello=multi("wekcke")
print(hello.var)

# print 15 as var is avaiable in programmer
# if var is not available in multi then it goes and search in programmer . As sequence of inheritence is  programmer and then Employee.If var is not in programmer then it search in Employee


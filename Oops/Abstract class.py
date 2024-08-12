from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0;
class Rectangle(shape):
    def __init__(self,length, breadth):
        self.length=length
        self.breadth=breadth
    def printArea(self):
        return self.length*self.breadth
    
rectangle=Rectangle(5,7)
print(rectangle.printArea())
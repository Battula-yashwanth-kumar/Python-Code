# Decorators as can be noticed by the name, is like a designer that helps to modify a function. THe decorators can be said to be a modification to  the external layer of function as it does not change its structure
#decorators takes a function and insert some new functionality in it without changing the function itself.




def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("THanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,10) # if you are sending params to the function then you need to add *args and **kwargs
# Iterables are objects that can be placed in loop of iteration. Ex: string, list, tuple
# Every iterable , either it is a string or tuple has a built in method __iter__() that creates an object when called.
# the object moves from character to character of iterable uisng the __next__() method

#Generator concept is aslo very similiar as it is used to make a iterator. The only difference comes in the return statement.
# generators does not uses a return statments.instead , it uses a yield keyword. yield functionality is very similar to return as it return a value to the caller , but the difference is that it aslo saves the state of the iteration.

def gen(n):
    for i in range(n):
        yield i

g=gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

h=5266796315
ier=iter(str(h))
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
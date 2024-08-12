# Join is a function in python that returns string by joining the elements of an iterable, using a string or character of our choice.
# In  the case of join function, the iterable can be list,dictionary, set, tuple or even a string itself
# The string that separates the iterations could be anything. It could just be a comma or a full length string. we can even use a blank space or newline character('\n') instead of a string
# syntax:string.join(iterable)
# if the iterable contains any non string values, join() will raise a TypeError exception

lis=["John","cena","wamnask","ajcklcka"]
# for item in lis:
#  print(item,"and",end=" ")
   
a=",".join(lis)
print(a)


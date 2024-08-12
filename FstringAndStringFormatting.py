import math

me="Hello"
a1=3
a="this is %s" %me
print(a)
a="this is %s %s" %(me,a1)
print(a)
a="this is {} {}"
b=a.format(me,a1)
print(b)
a="this is {1}{0}"
b=a.format(me,a1)
print(b)
a=f"this is {me} {a1} {2*12} {math.cos(65)}"
print(a)
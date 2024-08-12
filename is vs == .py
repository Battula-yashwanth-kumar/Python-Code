# Equality operator(==)
# It is also called as value equality
# Two object have the same value
# Identity operator (is)
# It is called as refernce equality
# Two references refer to the same object

x=[1,2,3]
y=x;
x==y  #true
y is x # true

x=[1,2,3]
y=[1,2,3]
x==y #true
x is y #false
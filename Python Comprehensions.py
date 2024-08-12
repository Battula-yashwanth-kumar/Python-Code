# Comprehensions in python can be defined as the pythonic way of writing code. using comprehension, we compress the code soit takes less space.
# Comprehension in python convert the four to five lines of code into a one liner.

# normal code :

ls=[]
for i in range(10):
    if i%3==0:
        ls.append(i)


#comprehension code :
ls=[i for i in range(5) if i%3==0]

print(ls)

dict1={i:f"item{i}" for i in range(1,100) if i%3==0}
dict1={i:f"item{i}" for i in range(1,100)}
dict2={value:key for key, value in dict1.items()}  #reversing the dictionary
print(dict2)
dresses=[dress for dress in ["jcklqk;asl","cjasclakcla","calskcs.akcsa;"]]
evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
for item in evens:
    print(item)

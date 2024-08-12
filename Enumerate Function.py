# Enumerate function does is it assigns an index to every element or value in the object that we want to iterate , so we do not have to assign a specific variable for incremental function.
l1=["clsc;CL","C SLKCNLA","Wkclwkv;nsld"]
for index, item in enumerate(l1):
    if index%2==0:
        print(f"{item}")
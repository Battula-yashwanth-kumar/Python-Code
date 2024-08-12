lists=[["sakcmsk","ncmmskcsal"],["svksdl","ascksclk"],["scjsdkcjsk","ncksclk"]]
dict1=dict(lists)
for item in dict1 :
    print(item)
for i,lo in dict1.items():
    print(i,lo)

Hello=["wkcksj","dsckasd",8,9,"cwjwkoiow"]

for item in Hello :
    if str(item).isnumeric() and item >=6 :  #str(item) because isnumberic() method only works when it is only in string format
        print(item);

for i in range(len(Hello)):

   print(Hello[i])
# "r" -open file for reading -default 
# "w" - open file for  writing
# "x" -create  file if not exists
#  "a" -add more content to a file
#  "t" text mode -default
# "b" -binary mode]
# "+" -read and write

f=open("Hello.txt","rt") #or f=open("Hello.txt")
print(f.readlines()) #prints the entire content in a line by line order
print(f.readline())
print(f.readline()) #reads line by line

content=f.read()
print(content)

for line in f:
    print(line,end='')

f.close()

# Writing and Appending File 

f=open("Hello.txt","w") # opeing in the right mode
a=f.write("Hlw;l;le;") #replaing the existing content with the provided text
print(a);
f.close();

# append mode
f=open("Hello.txt","a") # opeing in the right mode
a=f.write() #replaing the existing content with the provided text
print(a);
f.close();

# Handle Read and Write 

f=open("Hello", "rt")
print(f.read())
f.write("thank you")
f.close()


# Seek() and tell() functions

f=open("Hello.txt")
f.seek("H")  #brings the pointer to H character
print(f.tell()) #prints at which character the pointer is
print(f.readline()) #prints character from the H character
f.close()


# Using with Block to Open python files

with open("Hello.txt") as f :
    a=f.readlines()
    print(a)
    # we don't need to close in block


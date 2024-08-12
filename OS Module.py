# os module have lot of built in feature
# os.mkdir() --> to create directory
# os.rename() --> to rename the already existing directory
# os.rmdir()--> to remove the direcotry
# os.removeddirs() --> we can remove all directories within a directory by using removedirs()
#  os.environ.get() --> It will return us the environmment variables. The environment variables must be set or  the function will return null

import os
print(dir(os))
print(os.getcwd())
os.chdir("c://")
print(os.getcwd())
f=open("Hello.txt")
print(os.listdir("c://"))
os.makedirs("This/That")
os.rename("hello.txt","World.txt")
print(os.environ.get('path'))
print(os.path.join("c://","/hello.txt"))
print(os.path.exists("c://program file2"))
print(os.path.isfile("c://Program Files"))
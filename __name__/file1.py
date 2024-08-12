print("__name__ in tutmain1.py is set to" + __name__)

#using the main in our file, we can restrict same data from exporting to other files when imported
# we can restrict the unnecessary data, thusmaking the output cleaner and more readable
# we can chosse what others may import or what they may not while using our module.
# if __name__=="__main__" block prevents the certain code from being run when the module is imported.

def fun(string):
    return f"cmds,knvdncka.lz;{string}"

print(fun("vn dvms,md.."))

if __name__=="__main__":
    print("Hello wolrd")
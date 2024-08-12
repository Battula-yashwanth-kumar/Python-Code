# Exception is a Error that halts the program's normal functioning and displaying an Error onto the screen
# while the try and except block are for handling exceptions the raise keyword on the contrary is to raise an exception
# keyError: Raised when a mapping key is not found in the set of existing keys
# valueError: Raised when a function receives an argument with the  right type but an inappropriate value
# EOFError(End of file Error) : Raised when the input() function hits an end of the file condition without reading any data
# ImportError: Raised when the import statement has trouble trying to load a module
# NameError:Raised when a loacal or global name is not found
#ZeroDivisionError:Raised when the second argument of a division is zero

a=input("whatbisnyour ane,")
b=input("ckmckc;lq")
if b==0:
    raise ZeroDivisionError("bis o so stoping the program")
if a.isnumeric():
    raise Exception("number are not allowed")
c=input("Enter")

try:
    print(c)
except Exception as e:
    if c=='yash':
        raise ValueError('yash is blocked')
    print("Exception hanndled")

# we use an else keyword to print something in cases where no exception occurs
# Finally, will run in either case. It is also known as code cleaner because it will perform its action either an exception occur or not

f1=open("Hello.txt")
try:
    f=open("does2.txt")
except EOFError as e:
    print("ckdlcdc;d;c;;'w")
except IOError as e:
    print("cwkccds;")
else :
    print("THis will run only if except is not running")
finally:
    print("Run this anyways")
    f.close()
    f1.close()
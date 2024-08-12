l=10
def function(n):
    l=5;
    m=8
    l=l+45
    print(l,n)

function(5)

x=59
def hello():
    x=26
    def hello1():
        global x
        x=88
        print(x)
    hello1()

hello()
print(x)


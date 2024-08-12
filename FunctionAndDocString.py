# DocString is a short form of documentation string.Its purpose is to give the programmer a brief knowledge about the functionality of the function.
# it is optional and written """ """ triple Quotes.
# It is called by function._doc_ .

a=5
b=10
c=sum((a,b)) #inbuilt function

def function(d,e):
    """This function calculate average"""
    average=(d+e)/2;
    print(average);
    return average;

v=function(5,6)
print(v)
print(function.__doc__)  #prints the doc string in """"""
def factorial_iterative(n):
    fac=1
    for i in  range(n):
        fac=fac*(i+1);
    return fac

def factorial_recursive(n):
    if n==1:
        return 1;
    else : 
       return n*factorial_recursive(n-1)
    
print(factorial_iterative(10))
print(factorial_recursive(10))

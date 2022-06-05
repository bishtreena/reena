#arithmetic calculation using function 
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def mod(n1,n2):
    return n1%n2

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print( a,"+",b,"=", add(a,b))
print(a,"-",b,"=", sub(a,b))
print( a,"*",b,"=", mul(a,b))
print(a,"/",b,"=", div(a,b))
print(a,"%",b,"=", mod(a,b))




#find factorial of a number
n=int(input("enter number:"))
def factorial(n):
    fac=1
    for i in range(n):
         fac=fac*n
         n-=1
    return fac
print("\nfactorial of a {0} is".format(n))
print(factorial(n))

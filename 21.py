#find all divisors of integer
n=int(input("enter the integer:"))
for i in range (1,n):
    if n%i==0:
        print(i)

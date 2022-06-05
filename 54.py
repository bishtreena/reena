#find factors of a number
n=int(input("enter number:"))
print("factors of {0} is :".format(n))
for i in range (2,n+1):
    if n%i==0:
        print(i)
    else:
        pass

#find sum of even and odd numbers 
osum=0
esum=0
n=int(input("enter number:"))
for i in range (1,n):
    if (i%2)!=0:
        osum=osum+i
    else:
        esum=esum+i
print("sum of odd numbers:{0}".format(osum))
print("sum of even numbers:{0}".format(esum))

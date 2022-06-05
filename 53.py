#find the sum of fibonnaci series number
a=0
b=1
sum=0
n=int(input("enter the number of fibonacci series:"))
for i in range(n):
    print(' {0}'.format(a))
    sum=sum+a
    c=a+b
    a=b
    b=c
print("sum of series are:{0}".format(sum))











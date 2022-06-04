#find the average of two number
sum=0
for i in range (1,3):
    n=int(input("enter {0} number:".format(i)))
    sum=sum+n
avg=sum/2
print(" average of two number:{0}".format(avg))

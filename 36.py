#find sum and average of three number
sum=0
for i in range (1,4):
    n=int(input("enter {0} number:".format(i)))
    sum=sum+n
print("sum of three number :{0}".format(sum))
avg=sum/3
print(" average of three number:{0}".format(avg))


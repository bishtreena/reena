#find the sum  and average of natural number
sum=0
n=int (input("enter number:"))
for i in range(1,n):
    print(i)
    sum=sum+i
print("sum of number:{0}".format(sum))
avg=sum/(n-1)
print("average of number :{0}".format(avg))



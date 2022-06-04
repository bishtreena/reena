#find sum of odd numbers
sum=0
n=int(input("enter number:"))
for i in range (1,n):
    if (i%2)!=0:
        print(i)
        sum=sum+i
print("sum of odd numbers:{0}".format(sum))

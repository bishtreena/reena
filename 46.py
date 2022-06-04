#find sum of even numbers
sum=0
n=int (input("enter number:"))
for i in range (2,n):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum of even numbers:{0}".format(sum))

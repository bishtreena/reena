#check perfect number
num=int(input("enter the number:"))
num1=num
sum=0
for i in range(1,num1):
    if(num1%i==0):
      sum=sum+i
if(sum==num):
    print("{0} is a perfect number".format(num))
else:
    print("{0} is not a perfect number".format(num))

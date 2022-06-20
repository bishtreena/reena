#check neon number
num=int(input("enter number:"))
num1=num
sum=0
temp=num1**2
while(temp!=0):
  temp1=temp%10
  sum=sum+temp1
  temp=temp//10
if(num==sum):
    print("{0} is a neon number".format(num))
else:
    print("{0} is not a neon  number".format(num))

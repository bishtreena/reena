#check harshad number
num=int(input("enter number:"))
num1=num
sum=0
while(num1!=0):
  temp=num1%10
  sum=sum+temp
  num1=num1//10
print(sum)
if(num1%sum==0):
    print("{0} is a harshad number".format(num))
else:
    print("{0} is not a harshad number".format(num))

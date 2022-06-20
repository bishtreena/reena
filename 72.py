#check prime number
num=int(input("enter the number:"))
num1=num
sum=0
for i in range(2,num1):
  if(num1%i==0):
   break
else:
 print("{0} is a prime number".format(num1))

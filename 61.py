import math
digit=int(input("Enter the number of digits in number you want to enter: "))
num=int(input("enter the number:"))
s=num
sum=0
while (digit!=0):
    temp=s%10
    sum=pow(temp,digit)+sum
    s=s//10
    digit=digit-1
s=num  
if s==sum:
    print("{0} is a disarium number".format(s))
else:
    print("{0} is not a disarium number".format(s))    

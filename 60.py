#armstrong number
import math
digit=int(input("Enter the number of digits in number you want to enter: "))
num=int(input("enter the number:"))
s=num
sum=0
while (s!=0):
    temp=s%10
    sum=pow(temp,digit)+sum
    s=s//10
s=num  
if s==sum:
    print("{0} is a armstrong number".format(s))
else:
    print("{0} is not a armstrong number".format(s))    

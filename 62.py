#print disarium number from 1 to 100
import math
for num in range(1,101):
  length=len(str(num))
  s=num
  sum=0
  while (length!=0):
    temp=s%10
    sum=pow(temp,length)+sum
    s=s//10
    length=length-1
  s=num  
  if s==sum:
    print(s)

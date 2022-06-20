#print strong number from 1 to 100
for num in range (1,201):
  num1=num
  sum=0
  while(num1!=0):
    fact = 1
    temp=num1%10
    for i in range(1,temp+1):
      fact=fact*i
    sum=sum+fact
    num1=num1//10
  if(num==sum):
      print(num)


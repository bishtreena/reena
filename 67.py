#print harshad number from 1 to 100
for num in range(1,101):
  num1=num
  sum=0
  while(num1!=0):
    temp=num1%10
    sum=sum+temp
    num1=num1//10
  if(num%sum==0):
    print(num)

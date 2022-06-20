#print prime number from 1 to 100
for num in range(1,101):
  num1=num
  sum=0
  for i in range(2,num1):
    if(num1%i==0):
     break
  else:
    print(num)

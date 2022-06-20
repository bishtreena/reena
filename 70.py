#print palindrome number fro 1 to 100
for num in range (1,101):
  old=num
  length=len(str(num))
  result=0
  while(length!=0):
    temp=old%10
    result=result*10+temp
    old=old//10
    length=length-1
  if(result==num):
    print(num)
  

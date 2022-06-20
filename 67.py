#check krishnamurthy number
num=int(input("Enter number:"))
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
    print("{0} is a krisnamurthy number:".format(sum))
else:
    print("{0} is not a krisnamurthy number:".format(sum))

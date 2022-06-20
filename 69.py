#check palindrome number
num=int(input("Enter the number:"))
old=num
length=len(str(num))
result=0
while(length!=0):
    temp=old%10
    result=result*10+temp
    old=old//10
    length=length-1
if(result==num):
    print("{0} is a palindrome number:".format(num))
else:
    print("{0} is not a palindrome number:".format(num))

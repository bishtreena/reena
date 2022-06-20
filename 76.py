#check spy number
num=int(input("enter number:"))
mul=1
sum=0
num1=num
while(num1!=0):
    temp=num1%10
    sum=sum+temp
    mul=mul*temp
    num1=num1//10
if(sum==mul):
    print("{0} is a spy number".format(num))


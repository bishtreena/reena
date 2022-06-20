#find sum of digits in a number
digit=int(input("enter the digits in a number:"))
n=int(input("Enter the number:"))
sum=0
while(digit!=0):
    temp=n%10
    sum=temp+sum
    n=n//10
    digit=digit-1
print(sum)

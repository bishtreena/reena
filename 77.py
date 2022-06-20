#find prime factor of a number
num=int(input("Enter number:"))
num1=num
for i in range(2,num1):
    if(num1%i==0):
        count=1 
        for j in range(2,i//2+1):
           if(i%j==0):
            count=0
            break
        if count==1:
            print(i)  

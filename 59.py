#to find LCM Of two numbers
a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
if a>b:
    max=a
else:
    max=b
while(True):
    if max%a==0 and max%b==0:
        value=max
        break
    max+=1
print(value)




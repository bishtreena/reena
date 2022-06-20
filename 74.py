#check pronic number
n=int(input("enter a number:"))
s=0
for i in range(n):
    if i*(i+1)==n:
        s=1
        break
if(s==1):
    print("{0} is pronic a number".format(n))
else:
    print("{0} is not a pronic number".format(n))

#find sum of 10 number until users enter positive numbers
sum=0
for i in range (1,11):
    n=int(input("enter {0} number:".format(i)))
    if n<0:
        break
    else:
        sum=sum+n
print("sum of 10 numbers are:{0}".format(sum))


#to read 10 numbers and find their sum and average
sum=0
for i in range (1,11):
     n=int(input("enter {0} number:".format(i)))
     sum=sum+n
print(" sum of numbers are {0}".format(sum))
a=sum/10
print("average of numbers are {0}".format(a))


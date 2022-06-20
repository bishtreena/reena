#to count total characters in a string
var=input("Enter string:")
sum=0
for character in var:
    sum=sum+var.count(var)
print("total characters in a string are:{0}".format(sum))


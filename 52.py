a=0
b=1
n=int(input("enter the number of fibonacci series:"))
print("fibonacci series are:\n {0} \n {1}".format(a,b))
for i in range(n-2):
  c=a+b
  a=b
  b=c
  print(' {0}'.format(c))

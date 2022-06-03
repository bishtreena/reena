#find largest of three number
a=int(input("enter 1 number="))
b=int(input("enter 2 number="))
c=int(input("enter 3 number="))
if a>=b and a>=c:
      print('{0} is largest'.format(a))
elif b>=a and b>=c:
    print('{0} is largest'.format(b))
else:
    print('{0} is largest'.format(c))
               

#roots of a quadratic equation
import cmath
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b**2)-4*a*c
if d>0:
 root1=(-b-cmath.sqrt(d))/(2*a)
 root2=(-b+cmath.sqrt(d))/(2*a)
 print('two distinct real roots exists: root1 {0},root2{1}'.format(root1,root2))
elif d==0:
     root1=root2= -b/(2*a)
     print ('two equal and real root exist:root1 {0},root2{1}'.format(root1,root2))
elif d<0:
    root1=cmath.sqrt(-d)/(2*a)
    root2=cmath.sqrt(-d)/(2*a)
    print('two distinct complex roots exists:root1{0},root2{1}'.format(root1,root2))

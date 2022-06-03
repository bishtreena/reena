#to find compound interest
import math
p=int(input("enter principal balance:"))
r=float(input("enter interest rate:"))
r=r/100
print("interest rate{0}".format(r))
n=float(input("enter number of times interest per time period:"))
t=int(input ("enter time:"))
A=pow(p*(1+(r/n)),n*t)
print ('compound interest :{0}'.format(A))

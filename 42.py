#to find distance between two points
import math
x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("distance between two points:{0}".format(d))

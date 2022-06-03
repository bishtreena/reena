#find student grade
sub1=int(input("enter the marks of maths:"))
sub2=int(input("enter the marks of physics:"))
sub3=int(input("enter the marks of chemistry:"))
sub4=int(input("enter the marks of cs:"))
sub5=int(input("enter the marks of english:"))
total=(sub1+sub2+sub3+sub4+sub5)/5
per=total
print(" percentage of student is {0}".format(per))
if per>=65:
    print("A grade")
elif per<=64 and per>=45:
    print("B grade")
elif per<=44:
    print("c grade")
else:
    print("D grade")

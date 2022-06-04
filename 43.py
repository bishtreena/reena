#find total average and percentage of 5 subjects
sub1=int(input("enter the marks of maths:"))
sub2=int(input("enter the marks of physics:"))
sub3=int(input("enter the marks of chemistry:"))
sub4=int(input("enter the marks of cs:"))
sub5=int(input("enter the marks of english:"))
ta=(sub1+sub2+sub3+sub4+sub5)/5
print(" total average of 5 subjects:{0}".format(ta))
p=((sub1+sub2+sub3+sub4+sub5)/500)*100
print("percentage of 5 subjects:{0}%".format(p))

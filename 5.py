#arithmetic operations
a= float(input("enter first number") )
b= float(input("enter second number"))
c=int(input("press 1 for add,2 for sub,3 for mul,4 for modulus,5 for division"))
if c==1:
    sum=a+b
    print("sum of two number is",sum)
elif c==2:
    sub=a-b
    print("sub of two number is",sub)
elif c==3:
    mul=a*b
    print("mul of two number is",mul)
elif c==4:
    mod=a%b
    print("mod of two number is",mod)
elif c==5:
    div=a/b
    print("div of two number is ",div)
else:
    print("enter valid number")





#print negative number in  a range
start=int(input("enter the start of range:"))
end=int(input("enter the end of range:"))
for i in range(start,end):
    if(i<0):
        print(i)

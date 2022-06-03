#multiplication table
n=int (input(" table of :"))
a=int(input("enter the number:"))
for i in range(1,a+1,1):
    r=n*i
    print("{0}x{1}={2}".format(n,i,r))

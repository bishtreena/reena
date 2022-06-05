#count number of digits in a number
count=0
m=int(input("enter the number:"))
while(m!=0): 
    m//=10
    count+=1
print('number of digit in  a number:{0}'.format(count))


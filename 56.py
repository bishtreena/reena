#print first digit of a number
n=int(input("enter the number:"))
def firstdigit(n):
     while(n>=10): 
        n//=10
     return n
print(firstdigit(n))

#print last digit in a number
n=int(input("enter the number:"))
def firstdigit(n):
        n%=10
        return n
print(firstdigit(n))

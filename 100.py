#to count vowels in a string
var=input("Enter string:")
vowels=0
for i in var:
    if((i=='a'or i=='e'or i=='i' or i=='o' or i=='u')or(i=='A' or i=='E 'or i=='I' or i=='O' or i=='U')):
        vowels=vowels+1
print("number of vowels:{0}".format(vowels))
print(vowels)

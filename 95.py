#to count occurrence of a character in a string
var=input("Enter string:") 
print("occurence of each character in a string are:")
for character in var:
    print(character,var.count(character) )

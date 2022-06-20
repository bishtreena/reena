#print ASCII value of total characters in a string
text=input("Enter the string:")
ascii_values=[]
for character in text:
       ascii_values.append(ord(character))
print(ascii_values)

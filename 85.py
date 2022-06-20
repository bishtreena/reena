#check character is an alphabet,digit or special character
ch=input("Enter any chracter:")
if(ch.isdigit()):
    print("the given character",ch,"is a digit")
elif(ch.isalpha()):
    print('the given character',ch,'is a alphabet')
else:
    print('the given character',ch,'is a special character')
        

#to count characters frequency in a string
test=input("Enter string:")
res={}
for keys in test:
    res[keys]=res.get(keys,0)+1
print("count of all character in test\n"+str(res))   

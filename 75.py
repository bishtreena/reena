#print pronic number from 1 to 100
for n in range(1,101):
  s=0
  for i in range(n):
    if i*(i+1)==n:
        s=1
        break
  if(s==1):
    print(n)

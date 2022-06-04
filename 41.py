#to calculate electricity bill
h=int(input("enter the hours of use per month:"))
t=int(input("enter total appliances in kwh:"))
a=t/1000
totalbill=h/a
print("totalbill={0}".format(totalbill))

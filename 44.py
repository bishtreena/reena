#get current date and time
from datetime import datetime
now=datetime.now()
print("current date and time=",now)

dt_string=now.strftime("%d/%m/%y %H:%M:%S")
print("date and time=",dt_string)


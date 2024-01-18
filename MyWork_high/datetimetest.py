from datetime import (datetime as DateTime,\
                      timedelta as TimeDelta,\
                      date as Date)

currentDateTime = DateTime.now()
print(currentDateTime)
print("Date    : ",currentDateTime.date())
print("Day     : ",currentDateTime.day)
print("Month   : ",currentDateTime.month)
print("Year    : ",currentDateTime.year)
print("Time    :",currentDateTime.time())
print("Hours   :",currentDateTime.hour)
print("Minutes :",currentDateTime.minute)
print("Seconds :",currentDateTime.second)
print("Microseconds : ",currentDateTime.microsecond)
nextYear = DateTime(currentDateTime.year+1,currentDateTime.month,currentDateTime.day,22,59,59)
print("next year date : ",nextYear)


print("adding 100 days in current date : ",currentDateTime+TimeDelta(days=100))

print("representing datetime obj in string : ")
if(currentDateTime.day <10):
    day="0"+str(currentDateTime.day)
else:
    day = str(currentDateTime.day)
if(currentDateTime.month < 10):
    month = "0"+str(currentDateTime.month)
else:
    month = str(currentDateTime.month)
year = str(currentDateTime.year)
dateTimeStr = year+"-"+month+"-"+day+' 10:27:03.929149'
print(f"Date in stirng : {day}-{month}-{year}")
dateTimeObj = DateTime.strptime(dateTimeStr,'%Y-%m-%d %H:%M:%S.%f')
print("string to obj : ",dateTimeObj)
dateTimeStr = DateTime.strftime(dateTimeObj,'%d-%m-%Y')
print(dateTimeStr)






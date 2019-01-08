# get current hour of computer
import datetime
now = datetime.datetime.now()
print (now.hour, now.minute, now.second, sep=':')
print (now.day, now.month, now.year, sep='/')
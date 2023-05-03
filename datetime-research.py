# start with that 
# import datetime
#datetime module has datetime class that can contain information from both date and time objects
# print(datetime.datetime.now())
# print(datetime.date.today())

# date = datetime.date(2022, 5, 10)
# print(date)

# after
#main things datetime time date
from datetime import datetime, time, date

print(datetime.now())
today_date = date.today()
print(today_date)
print('year ', today_date.year)
print('month ', today_date.month)
print('day ', today_date.day)
timestamp = date.fromtimestamp(1326244364)
print(timestamp)

init_time = time() # initialized 0
print(init_time)
# particular time hour minute second
particular_time = time(12, 10, 50)
particular_time_with_attr = time(hour = 12, minute = 20, second = 33, microsecond = 11111)
print(particular_time)
print(particular_time_with_attr)
print('hour ', particular_time.hour)
print('minute ', particular_time.minute)
print('second ', particular_time.second)
print('microsecond ', particular_time.microsecond)

# first arguments year, month, day in the datetime() constructor are mandatory
dt = datetime(2023, 5, 3)
dt_with_time  = datetime(2023, 5, 3, 12, 50, 30, 435223)
print(dt)
print(dt_with_time)
print(dt_with_time.minute)

# timedelta
# represents the difference between two dates or times

first_date = date(2023, 5, 3)
second_date = date(2023, 4, 3)
delta = first_date - second_date
print(delta)

first_date_time  = datetime(2023, 5, 3, 12, 50, 30, 435223)
second_date_time  = datetime(2023, 4, 3, 11, 50, 20, 435223)
delta_date_time = first_date_time - second_date_time
print(delta_date_time)
print(type(delta_date_time))
# also we can get delta between two timedelta objects

# strptime strftime

# strptime() and strftime() are two methods in Python's built-in datetime module that deal with formatting 
# and parsing of dates and times.

#strptime - string parse time, is used to parse a string representing a date and time and convert it into a datetime object
date_string = "2023-05-03"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
# we can exchange m and d 
print('date_object ', date_object.day)

# strftime - string format time, to format a datetime object into a string
date_object = datetime.now()
date_string = date_object.strftime("%Y/%m/%d")
print(date_string)
print(type(date_string))

# In summary, strptime() is used to parse a string representing a date and time into a datetime object, 
# while strftime() is used to format a datetime object into a string representing a date and time according to a given format.

#time module 
# https://www.programiz.com/python-programming/time
import time
# In summary, the time module is mainly focused on providing access to low-level 
# time-related functionality, while the datetime module provides a higher-level, 
# more object-oriented approach to working with dates and times.
print('hello')
time.sleep(2)
print('after')
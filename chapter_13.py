import enum
class Weekdays(enum.Enum):
    Sunday = 6
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
#---------------------------------------------------------------------------

from datetime import datetime, date, timedelta
import time

# 13.1 Write the current date as a string to the text file today.txt.
today = datetime.today()
with open(file="todays_date.txt",mode="w+") as f:
    f.write(str(today))

# 13.2 Read the text file today.txt into the string today_string.
with open(file="todays_date.txt", mode="r") as f:
    d = f.read()[:19]
    print(d)

#   13.3 Parse the date from today_string.
    fmt = "%Y-%m-%d %H:%M:%S"
    today_string = time.strptime(d, fmt)
    print(today_string)
    print(datetime.strptime(d,fmt))

# 13.4 Create a date object of your day of birth.
dob = date(1981,3,13)

# 13.5 What day of the week was your day of birth?
print(Weekdays(dob.weekday()).name)

# 13.6 When will you be (or when were you) 10,000 days old?
ten_thousand = timedelta(days=10_000)
age_at_10000 = dob + ten_thousand
print(age_at_10000)


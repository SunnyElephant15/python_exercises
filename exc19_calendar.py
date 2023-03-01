import calendar
import datetime

time = datetime.datetime.now()
date = str(time.date())
date_split = date.split('-')
print(calendar.month(int(date_split[0]), int(date_split[1])))

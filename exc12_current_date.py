import datetime
date = str(datetime.datetime.now())
print(date)
date = date.partition(' ')
print(f'current date = {date[0]}')

from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Todo:
# You have code that needs to perform simple time conversions,
# like days to seconds, hours to minutes, and so on.

a = timedelta(days=2, hours=6, minutes=30)
b = timedelta(hours=4.5)

print(a + b)
print('Seconds :{}'.format(a.seconds))
print('Minutes :{}'.format(a.seconds/60))
print('Hours :{}'.format(a.seconds/3600))
print('Days:{}'.format(a.days))
print('Total Seconds :{}'.format(a.total_seconds()))
print('Total Minutes :{}'.format(a.total_seconds()/60))
print('Total Hours :{}'.format(a.total_seconds()/3600))

# get current datetime
curr_date = datetime.now()
print('Current Date time :',curr_date)

# add timedelta
print('Post add time delta :', curr_date + a)
print('Add 10 minutes :', curr_date + timedelta(minutes=10))

print('No of Days since New Year :',
      (datetime.today() - datetime(2018, 1, 1)).days)

print('Days to New Year :',
      (datetime(2019, 1, 1) - datetime.today()).days)

# Date after a month
print('Add 30 days to current time:', curr_date + timedelta(days=30))

print('Add 1 month', curr_date + relativedelta(months=+1))

#  finding a date for the last occurrence of a day of the week


def find_date_by_day(day, start_date=None):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
    if not start_date:
        start_date = datetime.today()

    week_day_num = start_date.weekday()
    target_week_day_num = weekdays.index(day)

    delta_days = abs(target_week_day_num - week_day_num - 7)
    #print(delta_days)

    if delta_days < 6:
        return start_date - timedelta(days=delta_days)
    else:
        return start_date


print(find_date_by_day('Wednesday',datetime(2018, 12, 12)))
print(find_date_by_day('Friday'))




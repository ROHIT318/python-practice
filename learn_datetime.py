import datetime as dt
import pytz

# create dates
date = dt.date(2026, 4, 5)
print(date)     # 2026-04-05

# get today date
today_dt = dt.date.today()
print(today_dt) # 2026-05-02

# get current day number
print(dt.date.weekday(today_dt))    # 5 -> 0=Monday, 6=Sunday
print(dt.date.isoweekday(today_dt)) # 6 -> 1=Monday, 7=Sunday

# get current week number
print(dt.date.today().strftime('%W'))   # 17 

# working with date and time together
dt_time = dt.datetime(2026, 5, 2, 12, 12, 12, 121212)
print(dt_time)                      # 2026-05-02 12:12:12.121212
dt_time = dt.datetime.now()
print(dt_time)                      # 2026-05-02 22:48:01.331114

# add or subtract dates from current dates 
today_dt_plus_8_days = dt.date.today() + dt.timedelta(days=8)
print(today_dt_plus_8_days)         # 2026-05-10
today_dt_time_plus_8_hours = dt.datetime.now() + dt.timedelta(hours=8)
print(today_dt_time_plus_8_hours)   # 2026-05-03 06:51:08.292524


# get time for utc
utc_dt_time_now = dt.datetime.now(dt.timezone.utc)
print(utc_dt_time_now)              # 2026-05-02 17:38:24.630818+00:00

# convert utc time to ist
ist_dt_time_now = dt.datetime.now(pytz.timezone('Asia/Kolkata'))
print(ist_dt_time_now)              # 2026-05-02 23:17:34.682236+05:30
ist_dt_time_now = utc_dt_time_now + dt.timedelta(hours=5, minutes=30)
print(ist_dt_time_now)              # 2026-05-02 23:14:37.620109+00:00

# convert datetime to a specific string format
ddmmyyyy_str = dt.datetime.strftime(ist_dt_time_now, '%d %b %Y')
print(ddmmyyyy_str)                 # 02 May 2026

# convert specific string format to datetime
ddmmyyyy_dt = dt.datetime.strptime(ddmmyyyy_str, '%d %b %Y')
print(ddmmyyyy_dt)                  # 2026-05-02 00:00:00

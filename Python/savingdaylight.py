import sys

for line in sys.stdin:
     val = line
     month, day, year, sunrise, sundown = val.split()
     sunrise_hour, sunrise_minute = sunrise.split(':')
     sundown_hour, sundown_minute = sundown.split(':')
     hour = int(sundown_hour) - int(sunrise_hour)
     minute = int(sundown_minute) - int(sunrise_minute)
     if minute<0:
         hour -= 1
         minute = 60 + minute
     print(month, day, year, hour, 'hours', minute, 'minutes')
     
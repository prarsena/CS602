import requests
from datetime import datetime, time

# Write up Instructions to get free API key.
apikey = "6276f196fd965d95349c4d3c233e20d8"

# Point to api documentation site
# https://openweathermap.org/api/one-call-api#history

# Figure out how to obtain timedate stamp for last 5 days.
SECONDS_IN_A_DAY = 60 * 60 * 24
now = datetime.today()
midnight = datetime.combine(now, time.min)

midnightLastNight = midnight.timestamp()
midnightYesterday = int(midnightLastNight) - SECONDS_IN_A_DAY
midnightTwoDaysAgo = midnightYesterday - SECONDS_IN_A_DAY
midnightThreeDaysAgo = midnightTwoDaysAgo - SECONDS_IN_A_DAY
midnightFourDaysAgo = midnightThreeDaysAgo - SECONDS_IN_A_DAY

datestamps = [int(midnightLastNight), midnightYesterday, midnightTwoDaysAgo, midnightThreeDaysAgo, midnightFourDaysAgo ]
for i in datestamps:
    print(i)
    print(datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S %Z'))

# make 5 calls to the daily/ hourly data.
# for i in datestamps:
#     uri = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.99&lon=30.9&dt=1623185907&units=imperial&appid=" + apikey
#     response = requests.request("GET", uri)
#     print(response.text)

# 5 days (datestamp calls) worth of
#list = [{}, {}, {}, {}, {}]

# document unix datetime to python str.ftime
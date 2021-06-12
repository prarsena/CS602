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

datestamps = [int(midnightLastNight), midnightYesterday, midnightTwoDaysAgo, midnightThreeDaysAgo, midnightFourDaysAgo]
#datestamps = [int(midnightLastNight), midnightFourDaysAgo]

# for i in datestamps:
#     print(i)
#     print(datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S %Z'))
LAT = 43.3602
LON = -71.0551

LONDON_LAT = 51.5074
LONDON_LON = -0.118092
weatherData = []
# make 5 calls to the daily/ hourly data.
for date in datestamps:
     uri = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=43.3602&lon=-71.0551&dt="+str(date)+\
           "&units=imperial&appid=" + apikey
     response = requests.request("GET", uri)
     #print(response.text)
     weatherData.append(response.json())

# weatherData is a list, which contains 5 entries.
# The list entries are dictionaries.
# list = [{}, {}, {}, {}, {}]

# Traverse the list:
for dayOfWeatherData in weatherData:

    # Return info about each hour in reverse order.
    for hour in range(23,-1,-1):
        hourlyDatestamp = dayOfWeatherData.get('hourly')[hour].get('dt')

        #print(hourlyDatestamp)
        # document unix datetime to python str.ftime
        timeInfo_utc = datetime.utcfromtimestamp(hourlyDatestamp).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeInfo_mytime = datetime.fromtimestamp(hourlyDatestamp).strftime('%Y-%m-%d %H:%M:%S %Z')
        tempInfo = dayOfWeatherData.get('hourly')[hour].get('temp')
        feelInfo = dayOfWeatherData.get('hourly')[hour].get('feels_like')
        print("Unix Datestamp: ", hourlyDatestamp)
        print("UTC: " + timeInfo_utc)
        print("EDT: " + timeInfo_mytime)
        print("Temp (F): ", tempInfo)
        print("Temp Feel (F): ", feelInfo)
        print()


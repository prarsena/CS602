import requests
from datetime import datetime, time

## https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=43.3602&lon=-71.0551&dt=1623384000&units=imperial&appid=6276f196fd965d95349c4d3c233e20d8

SECONDS_IN_A_DAY = 60 * 60 * 24

def getWeather(apikey, latitude, longitude):
    now = datetime.today()
    midnight = datetime.combine(now, time.min)

    midnightLastNight = midnight.timestamp()
    midnightYesterday = int(midnightLastNight) - SECONDS_IN_A_DAY
    midnightTwoDaysAgo = midnightYesterday - SECONDS_IN_A_DAY
    midnightThreeDaysAgo = midnightTwoDaysAgo - SECONDS_IN_A_DAY
    midnightFourDaysAgo = midnightThreeDaysAgo - SECONDS_IN_A_DAY

    datestamps = [int(midnightLastNight), midnightYesterday, midnightTwoDaysAgo, midnightThreeDaysAgo,
                  midnightFourDaysAgo]
    weatherData = []
    for date in datestamps:
        uri = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + str(latitude) + \
              "&lon=" + str(longitude) + "&dt=" + str(date) + \
              "&units=imperial&appid=" + apikey
        response = requests.request("GET", uri)
        weatherData.append(response.json())

    return weatherData

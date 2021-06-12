import weather
from datetime import datetime, time
import pprint

# Find a Latitude and Longitude of a US city here:
# https://www.latlong.net/category/cities-236-15.html
latitude = 43.3602
longitude = -71.0551

# Write up Instructions to get free API key.
apikey = "6276f196fd965d95349c4d3c233e20d8"

pp = pprint.PrettyPrinter(indent=2)
weatherData = weather.getWeather(apikey, latitude, longitude)
# print(pp.pprint(data))

timezoneOffset = weatherData[0]['timezone_offset']

for day in weatherData:

    for hour in reversed(day['hourly']):
        hourlyDateStamp = hour['dt']
        hourString = datetime.utcfromtimestamp(hourlyDateStamp + timezoneOffset).strftime('%Y-%m-%d %H:%M:%S')
        hourlyTemperature = hour['temp']
        hourlyFeelsLike = hour['feels_like']
        print("Unix time: ", hourlyDateStamp)
        print("Time: " + hourString)
        print("Temp: ", hourlyTemperature)
        print("Feels: ", hourlyFeelsLike)
        print()
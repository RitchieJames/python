import requests
from datetime import datetime
import pytz
my_lat = float(input("enter the latitude "))
my_long = float(input("enter the longitude "))

# Create a dictionary called parameters
parameters = {
    "lat": my_lat,
    "lng": my_long,
}



response  = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise_utc  = response.json()["results"]["sunrise"]

sunset_utc  = response.json()["results"]["sunset"]

dubai_tz = pytz.timezone('Asia/Dubai')
sunrise_datetime_utc = datetime.strptime(sunrise_utc, "%I:%M:%S %p")
sunset_datetime_utc = datetime.strptime(sunset_utc, "%I:%M:%S %p")
sunrise_datetime_gst = dubai_tz.localize(sunrise_datetime_utc).strftime('%Y-%m-%d %H:%M:%S %Z%z')
sunset_datetime_gst = dubai_tz.localize(sunset_datetime_utc).strftime('%Y-%m-%d %H:%M:%S %Z%z')


#print(f"sunrise time is {sunrise} UTC\n sunset time is {sunset} UTC")
#print(my_datetime_cet)

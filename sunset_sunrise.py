import requests
print("use https://www.latlong.net/ to find the latitude and longitude of the desired place ")
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


print(f"sunrise time is {sunrise_utc} UTC\n sunset time is {sunset_utc} UTC")


import requests

API_Key="4b4f8cbeaf12486c58bbfc729f2cf8b7"
TCity= input("Enter your city: ")

geo_url= "http://api.openweathermap.org/geo/1.0/direct"
geoPar={
    "q": TCity,
    "limit": 1,
    "appid": API_Key
}

city_response=requests.get(geo_url, geoPar)
city_data= city_response.json()

if city_data:
    city_lat=city_data[0]["lat"]
    city_lon=city_data[0]["lon"]
    print(city_lat,city_lon)
else:
    print("Could not find city! Sorry.")

weather_url="http://api.openweathermap.org/data/2.5/weather"
weather_par={
    "lat":city_lat,
    "lon":city_lon,
    "units": "Imperial",
    "appid":API_Key
}

weather_response= requests.get(weather_url,weather_par)
if weather_response.status_code==200:
    weather_data= weather_response.json()
    currentCityTemp=weather_data["main"]["temp"]
    print("Current temperature in ", TCity, " is " ,currentCityTemp," Farenheit!")
else:
    print("Failed to retrieve data")
    print("Status Code:", weather_response.status_code)


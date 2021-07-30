import requests
import os
from datetime import datetime


location=input("Enter the City Name: ")
user_api=os.environ['Current_Weather_Data']

complete_api_link='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+user_api
api_link=requests.get(complete_api_link)
api_data=api_link.json()

print('-------------------------------------------------')
weather_=api_data['weather'][0]['description']
temp_=((api_data['main']['temp'])-273.15)
wind_speed=api_data['wind']['speed']
print(weather_)
print(temp_)
print(wind_speed)


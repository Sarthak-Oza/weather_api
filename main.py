import requests


#API Key 
API_KEY = API_KEY_ENV


#Take input for city name
city_name = input("Please enter city name: ")

#Try/except to raise error message
try:
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric")
except:
    raise Exception("Please try another city!")

json_data = weather_data.json()
result_weather_dict = {"weather:": json_data["weather"][0]["main"], "Temp:": json_data["main"]["temp"]}
for key, value in result_weather_dict.items():
    print(f"{key} -> {value}")




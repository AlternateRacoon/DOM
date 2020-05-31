import requests


def get_weather():
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=Karachi&APPID=07bbb96304be02263bcfa5534021d1c6")

    x = response.json()

    y = x["main"]

    current_temperature = y["temp"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]
    temprature = str(int(current_temperature - 273.15)) + " degrees"
    humidity = str(current_humidity) + "%"
    return "Currently it is " + temprature + " outside. The description being " + weather_description + ". The Humidity is about " + humidity

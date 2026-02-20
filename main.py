import requests # requests package
from twilio.rest import Client # twilio package



api_key =  os.eviron.get("OWM_API_KEY") # account API KEY
own_endpoint = "https://api.openweathermap.org/data/2.5/forecast" # API URl
account_sid = os.environ.get("SID")  # account SID
auth_token = os.environ.get("AUTH")     # account TOKEN



# API parameters
weather_parameters = {
    "lat": 9.657066, # these are not my latitude and longitude
    "lon": -212.283752,
    "appid": api_key,
    "cmt": 4,

}

response = requests.get(own_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json() # data in JSON formate



will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if 600 >int(condition_code) <= 700: # Please go through the condition document for specific weather
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid="[your message service ID]",
            body="It is going to rain bring ☔☂️🌂",
            to="[your mobile number]"  # Your mobile number
        )
        print(message.status)
    elif 100 > int(condition_code) <= 200:
        client = Client(account_sid , auth_token)
        message = client.messages.create(
            messaging_service_sid = "[your message service ID]",
            body = "Stay in home Thunderstorm chances ⛈️⚡",
            to="[your mobile number]"
        )
        print(message.status)
    elif  200 >int(condition_code) <= 300:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            messaging_service_sid = "[your message service ID]",
            body = " Light intensity, heavy, or shower drizzle is coming 🌧️🌧️",
            to="[your mobile number]"
        )
        print(message.status)

    elif  300 > int(condition_code) <= 500:
        client = Client(account_sidd,auth_token)
        message = client.messages.create(
            messaging_service_sid = "[your message service ID]",
            body = "Light rain don't forget to take umbrella 🌂🌂",
            to = "C"
        )
        print(message.status)

    elif  500 > int(condition_code) <= 600:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            messaging_service_sid = "[your message service ID]",
            body = "Hey it's going to snow fall ❄️🌨️🌨️",
            to = "[your message service ID]"
        )
        print(message.status)


# output -> "Accepted" | SMS sent






























import requests
from arsewards import arsewards_dict 

api_key = arsewards_dict["weatherAPI"] 

parameters = {
    "lat" : 52.5552,
    "lon" : -8.56818,
    "appid": api_key,
    "cnt": 4,
}
parameters = {
    "lat" : -5.33,
    "lon" : -151.48,
    "appid": api_key,
    "cnt": 4,
}

res = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast",params = parameters).json()

gonnaRain = False
for weather in res["list"]:
    code = int(weather["weather"][0]["id"])
    print(code)
    if code < 700:
        gonnaRain = True

if gonnaRain:
    print("gonna rain")
res

from twilio.rest import Client

twilio_account_sid = arsewards_dict["twilio_account_sid"]
twilio_auth_token = arsewards_dict["twilio_auth_token"]
the_number = arsewards_dict['the_number']
client = Client(twilio_account_sid, twilio_auth_token)

if gonnaRain:
    message = client.messages.create(
      from_='+12177658194',
      body='It\'s gonna rain, bring an umbrella!',
      to='+3530860569107'
    )

print(message.status)
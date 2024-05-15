import requests
from arsewards import arsewards_dict 
import vonage

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

#res = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast",params = parameters).json()
#
#gonnaRain = False
#for weather in res["list"]:
#    code = int(weather["weather"][0]["id"])
#    print(code)
#    if code < 700:
#        gonnaRain = True
#
#if gonnaRain:
#    print("gonna rain")
#res
#
#from twilio.rest import Client
#
#twilio_account_sid = arsewards_dict["twilio_account_sid"]
#twilio_auth_token = arsewards_dict["twilio_auth_token"]
#the_number = arsewards_dict['the_number']
#client = Client(twilio_account_sid, twilio_auth_token)
#
#if gonnaRain:
#    message = client.messages.create(
#      from_='+12177658194',
#      body='It\'s gonna rain, bring an umbrella!',
#      to='+3530860569107'
#    )
#print(message.status)
#
#
#vonage_key =arsewards_dict["vonage_account_sid"]
#vonage_api= arsewards_dict["vonage_auth_token"]
#number = arsewards_dict["my_number"]
#
#client = vonage.Client(key=vonage_key, secret=vonage_api)
##client.messages.send_message()
#client.messages.send_message(
#    {
#        "channel": "whatsapp",
#        "message_type": "text",
#        "to": number,
#        "from": "14157386102",
#        "text": "This is a WhatsApp text message sent using the Vonage Messages API",
#    }
<<<<<<< HEAD
<<<<<<< HEAD
#)
=======
=======
>>>>>>> parent of 15c4ca7 (Removing secrets)
#)

# Specify the phone number (with country code) and the message
import pywhatkit as kit
phone_number = "+353860569107"
message = "Hello from Python! This is an instant WhatsApp message."

# Send the message instantly
<<<<<<< HEAD
kit.sendwhatmsg_instantly(phone_number, message,13, 12, 1)
>>>>>>> parent of 15c4ca7 (Removing secrets)
=======
kit.sendwhatmsg_instantly(phone_number, message,13, 12, 1)
>>>>>>> parent of 15c4ca7 (Removing secrets)

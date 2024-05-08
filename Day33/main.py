import requests
from datetime import datetime
import smtplib
from arsewards import arsewards_dict
my_email = "KevinsFancyTester12@gmail.com"
destination_email = arsewards_dict["kevinsHiddenEmail"]
password =   arsewards_dict[my_email]
gmPass = arsewards_dict["KevinsFancyGmAppPassword"]
gmail_link = "smtp.gmail.com"



MY_LAT = 52.665074 # Your latitude
MY_LONG =-8.568145 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
# Overriding so that they're  equal
iss_latitude = MY_LAT
iss_longitude = MY_LONG


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
time_now = int(time_now.split(" ")[1].split(":")[0])

# Testing 
time_now = int("00")
#print(time_now)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if MY_LAT +5 > iss_latitude and MY_LAT -5 <iss_latitude and MY_LONG +5 > iss_longitude and MY_LONG -5 < iss_latitude: 
    print ("It's here!")
    if time_now < sunrise or time_now > sunset:
        print("Look up")
        with  smtplib.SMTP(host = gmail_link) as connection:
            #    body = f"Happy birthday {birthday['name']} \n Hope you have a beautiful day and eat lots of cake"
            subject = f"ISS Overhead"
            connection.starttls()
            body = "Look Up!"
            connection.login(user= my_email, password = gmPass)
            connection.sendmail(msg = f"Subject:{subject} \n\n{body}", from_addr=my_email, to_addrs=destination_email)
            connection.close() 
    else:
        print("It's invisible :( ")

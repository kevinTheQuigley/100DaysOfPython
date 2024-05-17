import requests
from datetime import datetime
import os


#nutri_app_id = arsewards_dict["nutri_app_id"]
#nutri_app_key = arsewards_dict["nutri_app_key"]
#sheety_code = arsewards_dict["sheety_code"]
#sheety_auth= arsewards_dict["sheety_auth"]
nutri_app_id = os.environ.get("NUTRI_APP_ID","Sorry, that needs to be added")
nutri_app_key= os.environ.get("NUTRI_APP_KEY","Sorry, that needs to be added")
sheety_auth  =  os.environ.get("SHEETY_AUTH","Sorry, that needs to be added")
sheety_code  = os.environ.get("SHEETY_CODE","Sorry, that needs to be added")
print(nutri_app_id)


workout = input("What exercise did you do today?!")
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_params = {
    "query":workout
}

headers = {
    'Content-Type': 'application/json',
    "x-app-id":nutri_app_id,
    "x-app-key":nutri_app_key,
}

#Creating the nutri
response = requests.post(url = nutri_endpoint,json = nutri_params,headers = headers)
print(response.text)

cal = response.json()["exercises"][0]["nf_calories"]
exercise = response.json()["exercises"][0]["name"]
duration= response.json()["exercises"][0]["duration_min"]
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_endpoint= f"https://api.sheety.co/{sheety_code}/kevsWorkouts/workouts"

sheety_params = {
    "workout" : {
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":cal
    }
}
sheety_header = {
    "Authorization":sheety_auth

}
response = requests.post(url = sheety_endpoint,json = sheety_params,headers= sheety_header)
print(response.text)
print(response.json())
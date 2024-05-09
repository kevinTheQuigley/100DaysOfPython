import requests
import html

parameterss = {"amount":10,"category":18,"type":"boolean"}
api_location = "https://opentdb.com/api.php"
response = requests.get(url = api_location,params= parameterss)
#print(response.json()["results"])

question_data = response.json()["results"]
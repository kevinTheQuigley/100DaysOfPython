import requests
from datetime import datetime,date
from arsewards import arsewards_dict

#User_Creation
pixela_endpoint = "https://pixe.la/v1/users"

#
pixela_token = arsewards_dict["pixela_token"]
pixela_user= arsewards_dict["pixela_user"]
pixela_graph_id= arsewards_dict["graph_id"]

user_params = {
    "token":pixela_token, 
    "username": pixela_user,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#response = requests.post(url=pixela_endpoint,json = user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_user}/graphs"

graph_params = {
    "id":pixela_graph_id,
    "name":"Daily Meditation Record",
    "unit":"Minutes",
    "type":"int",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":pixela_token
}
#Creating the graph
#response = requests.post(url = graph_endpoint,json = graph_params,headers = headers)
#https://pixe.la/v1/users/kevinthequigley/graphs/mediminutes.html


pixel_endpoint = f"{pixela_endpoint}/{pixela_user}/graphs/{pixela_graph_id}"

pixel_params = {
    "date":datetime.now().strftime("%Y%m%d"),
    "quantity":"20",
    #"optionalData":"It was a good day"
}

response = requests.post(url = pixel_endpoint,json = pixel_params,headers = headers)

print(response.text)

#Removing a pixel
day = date(year = 2024,month = 5,day = 15).strftime("%Y%m%d")
pixel_put_endpoint = f"{pixela_endpoint}/{pixela_user}/graphs/{pixela_graph_id}/{day}"

pixel_put_params = {
    "date":datetime.now().strftime("%Y%m%d"),
    "quantity":"10",
    #"optionalData":"It was a good day"
}
#response = requests.put(url = pixel_put_endpoint,json = pixel_put_params,headers = headers)

print(response.text)
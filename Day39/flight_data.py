#from requests import response
import requests
from arsewards import arsewards_dict 







class FlightData:
    def __init__(self,destination) -> None:
        self.destination = destination
    #This class is responsible for structuring the flight data.
    #payload = {
    #    "market": "IE",
    #    "locale": "en-GB",
    #    "currency": "EUR",
    #    "adults": 1,
    #    "children": 0,
    #    "infants": 0,
    #    "cabinClass": "economy",
    #    "stops": ["direct", "1stop", "2stops"],
    #    "flights": [
    #        {
    #            "fromEntityId": "DUB",
    #            "toEntityId": "SYD",
    #            "departDate": "2024-06-21"
    #        },
    #        {
    #            "fromEntityId": "DUB",
    #            "toEntityId": "SOF",
    #            "departDate": "2024-06-28"
    #        }
    #    ]
    #}
    querystring = {
                "fromEntityId":"DUB",
                "toEntityId":"SYD"
                }

    headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": arsewards_dict['X-RapidAPI-Key'],
    	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }
    headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": arsewards_dict['X-RapidAPI-Key'],
    	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }


    #url = "https://sky-scanner3.p.rapidapi.com/flights/search-multi-city"
    url = "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"

    def get_flight_data(self):
        self.response = requests.get(self.url, headers=self.headers, params=self.querystring)
        #self.response = requests.post(self.url, json=self.payload, headers=self.headers)
        return(self.response.json())
    
    def get_prices(self):
        self.prices = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            self.prices.append(itenerary["price"]["raw"])
            return(self.prices)

    def get_legs(self):
        self.legs = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            self.legs.append(itenerary["legs"][:]["destination"]["name"])
            return(self.legs)

    def get_carriers(self):
        self.carriers = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            self.carriers.append(itenerary["legs"][:]["carriers"]["marketing"][:]["name"])
            return(self.carriers)

    def get_selfTransfers(self):
        self.selfTransfers = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            self.selfTransfers.append(itenerary["legs"]["isSelfTransfer"])
            return(self.selfTransfers)
            
        print(self.response.text)

    def generate_text_itenerary(self):
        self.textReturn = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            pass

        

flight_data = FlightData("Sydney")
print(flight_data.get_flight_data())

print(flight_data.get_prices())
print(flight_data.get_legs())
print(flight_data.get_carriers())
print(flight_data.get_selfTransfers())



print("debuggin")
print("And de-buggin")
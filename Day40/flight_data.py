#from requests import response
import requests
from arsewards import arsewards_dict 







class FlightData_roundtrip:
    def __init__(self,destination,duration) -> None:
        self.destination = destination
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
    #url_oneway = 'https://sky-scanner3.p.rapidapi.com/flights/search-one-way',
    url= "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"

    def get_flight_data(self):
        self.response = requests.get(self.url, headers=self.headers, params=self.querystring)
        #self.response = requests.post(self.url, json=self.payload, headers=self.headers)
        return(self.response.json())
    
    def get_prices(self):
        self.prices = []
        for itenerary in self.response.json()["data"]["flightQuotes"]["results"]:
            #flight_data.response.json()["data"]["flightQuotes"]["results"][0]['content']['price']
            self.prices.append(itenerary["content"]["rawPrice"])
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


class FlightData_oneway:
    def __init__(self,destination,duration) -> None:
        self.destination = destination
        self.duration =duration

        self.querystring = {
                    "fromEntityId":"DUB",
                    "toEntityId":self.destination,
                    "duration":self.duration*60,
                    "stops":0
                    #51 hour - 3090
                    #28 hour - 1680
                    }

    headers = {
    	#"content-type": "application/json",
    	"X-RapidAPI-Key": arsewards_dict['X-RapidAPI-Key'],
    	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }


    url= 'https://sky-scanner3.p.rapidapi.com/flights/search-one-way'

    def get_flight_data(self):
        self.response = requests.get(self.url, headers=self.headers, params=self.querystring)
        return(self.response.json())
    
    def get_prices(self):
        self.prices = []
        for itenerary in self.response.json()["data"]["flightQuotes"]["results"]:
            #flight_data.response.json()["data"]["flightQuotes"]["results"][0]['content']['price']
            self.prices.append(itenerary["content"]["rawPrice"])
        return(self.prices)
    
    
    def get_dates(self):
        self.dates = []
        for itenerary in self.response.json()["data"]["flightQuotes"]["results"]:
            #flight_data.response.json()["data"]["flightQuotes"]["results"][0]['content']['price']
            self.dates.append(itenerary["content"]["outboundLeg"]['localDepartureDateLabel'])
        return(self.dates)

    #for itenerary in flight_data.response.json()["data"]["flightQuotes"]["results"]:
    #    print(itenerary["content"]["price"])
    #flight_data.response.json()["data"]["flightQuotes"]["results"][0]['content']['price']
    #self.prices.append(itenerary["content"]["price"])
    #return(self.prices)

#    def get_legs(self):
#        self.legs = []
#        for itenerary in self.response.json()["data"]["flightQuotes"]["results"]:
#            self.legs.append(itenerary["legs"][:]["destination"]["name"])
#        return(self.legs)

#    for itenerary in flight_data.response.json()["data"]["flightQuotes"]["results"]:
#        #print(itenerary["content"]["price"])
#        print(itenerary["legs"]["price"][:]["destination"]["name"])

#    def get_carriers(self):
#        self.carriers = []
#        for itenerary in self.response.json()["data"]["flightQuotes"]["results"]:
#            self.carriers.append(itenerary["legs"][:]["carriers"]["marketing"][:]["name"])
#        return(self.carriers)
#
#    def get_selfTransfers(self):
#        self.selfTransfers = []
#        for itenerary in self.response.json()["data"]["itineraries"]:
#            self.selfTransfers.append(itenerary["legs"]["isSelfTransfer"])
#        return(self.selfTransfers)
#            
#        print(self.response.text)

    def generate_text_itenerary(self):
        self.textReturn = []
        for itenerary in self.response.json()["data"]["itineraries"]:
            pass



#flight_data = FlightData_oneway("SYD",28)
#print(flight_data.get_flight_data())
#
#print(flight_data.get_prices())
#print(flight_data.get_dates())
#print(flight_data.get_legs())
#print(flight_data.get_carriers())
#print(flight_data.get_selfTransfers())



print("debuggin")
print("And de-buggin")
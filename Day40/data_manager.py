import requests
class DataManager:
    def __init__(self) -> None:
        url = "https://api.sheety.co/7578b074a021d96b936b9161968196fb/kevsFlightDeals/prices"
        self.response = requests.get(url).json()
        self.iataCodes = []
        self.durations = []
        self. prices = []
        for j in self.response['prices']:
            self.iataCodes.append(j['iataCode'])
            self.durations.append(j['duration'])
            self.prices.append(j['lowestPrice'])
    #This class is responsible for talking to the Google Sheet.
    pass
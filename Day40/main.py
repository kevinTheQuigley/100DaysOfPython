#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import flight_data
import data_manager
import notification_manager

dataManager = data_manager.DataManager()
notificationManager = notification_manager.NotificationManager()

Trips = []

for i in range(len(dataManager.iataCodes)):
    trip = flight_data.FlightData_oneway(dataManager.iataCodes[i],dataManager.durations[i])
    trip.get_flight_data()
    trip.get_dates()
    trip.get_prices()
    for j in range(len(trip.prices)):
        if int(trip.prices[j])< int(dataManager.prices[i]):
            Trips.append(trip)
            notificationManager.take_message(f"From Dublin to {trip.destination} for {trip.prices[i]} on {trip.dates[i]}\n")
notificationManager.produce_message()
notificationManager.send_message()


import csv 

with open("weather_data.csv") as data:
    lineList = csv.reader(data)
    print(type(lineList))
    temps = []
    for line in lineList:
        temps.append((line[1]))
    temps = temps[1:]
    for i in range(len(temps)):
        temps[i] = int(temps[i])
    print(temps)
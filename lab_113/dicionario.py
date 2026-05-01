import csv
import copy
import os
from tabulate import tabulate

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'car_fleet.csv')

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

myInventoryList = []

with open(csv_path) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            lineCount += 1
        else:
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"]      = row[0]
            currentVehicle["make"]     = row[1]
            currentVehicle["model"]    = row[2]
            currentVehicle["year"]     = row[3]
            currentVehicle["range"]    = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"]= row[6]
            currentVehicle["mileage"]  = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.\n')


# Renomeia as chaves para cabeçalhos mais legíveis
headers = {
    "vin": "VIN",
    "make": "Make",
    "model": "Model",
    "year": "Year",
    "range": "Range (mi)",
    "topSpeed": "Top Speed",
    "zeroSixty": "0-60 (s)",
    "mileage": "Mileage"
}

print(tabulate(
    myInventoryList,
    headers=headers,
    tablefmt="rounded_outline"
))
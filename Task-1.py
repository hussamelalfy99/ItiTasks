import csv
# here the output will be a dictionnary_tupled values !!
with open('car_fleet.csv', mode='r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
for row in data:
    print(row)
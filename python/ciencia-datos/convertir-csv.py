import csv

with open('tabla-sustraccion.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])
        print(row[2])

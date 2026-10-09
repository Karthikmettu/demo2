import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)   # skip header

    for row in reader:
        if int(row[1]) > 21:
            print(row)
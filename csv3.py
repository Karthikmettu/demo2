import csv

with open("students.csv", "a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["RAM",25])

   
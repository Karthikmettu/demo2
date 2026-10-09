import csv

data = [
    ["name", "age", "course"],
    ["Karthik", 20, "CSE"],
    ["Ravi", 21, "ECE"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file written successfully")
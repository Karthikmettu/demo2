import json

# Read existing records
with open("data.json", "r") as file:
    data = json.load(file)

# New record
new_record = {
    "name": "Ravi",
    "age": 22,
    "skills": ["java", "networking"]
}

# Add new record
data.append(new_record)

# Save back to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("New record added successfully")
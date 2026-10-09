import json
data={"name":"karthik", "age":20, "skills":["python", "cyber security"]}

with open("data.json","w") as file:
    json.dump(data,file)
    print("created successfully")

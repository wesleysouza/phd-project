import json

#Simulando dados da casa
hems = {
    "name": "house1",
    "appliances": ["a1", "a2", "a3"],
    "number": 10
}

# Convert in JSON

y = json.dumps(hems)

print(y)

# Load Json in Python

json_data = json.loads(y)
print(json_data["appliances"])
import json

data = {
    "username" : "ismael_001",
    "email" : "ismael_khan@gmail.com"
}

json_data = json.dumps(data, sort_keys=True)

print(json_data)
# print(data)
# print(type(json_data))
# print(type(data))
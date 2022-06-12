import json

data_dict = {
    'username' : 'sir_newton',
    'email' : 'issac_newton@gmail.com'
}

# json.dumps() converts a dictionary to a json string
data_json = json.dumps(data_dict, sort_keys=True)  # 'sort_keys' is an optional parameter. If True, then it sorts the keys


# json.loads() converts a json string to a dictionary
data = json.loads(data_json)


################# Avoid confusion #################

# json.loads() is used to convert a JSON string to a dictionary  whereas,  json.load() is used for reading from a JSON file/document

# json.dumps() is used to convert a dictionary to a JSON string  whereas,  json.dump() is used for storing a python object in a file
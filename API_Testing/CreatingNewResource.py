# import requests
# import json
#
# #api url
# url = "https://reqres.in/api/users"
#
# #read input json from file
# file = open("C:\\Users\\DELL\\OneDrive\\Desktop\\CreateUser.json",'r')
# json_input = file.read()
# request_json = json.loads(json_input)
# #print(request_json)
#
# #make post request with json input body
#
# response = requests.post(url,json=request_json)
# assert response.status_code ==201

import requests
import json

# API URL
url = "https://reqres.in/api/users"

# Read JSON from file
with open("C:\\Users\\DELL\\OneDrive\\Desktop\\CreateUser.json", 'r') as file:
    request_json = json.load(file)

# Send POST request
response = requests.post(url, json=request_json)

# Print response info
print("Status Code:", response.status_code)
print("Response Body:", response.text)

# Assert
assert response.status_code == 201, f"Expected 201 but got {response.status_code}"

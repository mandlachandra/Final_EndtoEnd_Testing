#Q1: How do you convert an API response to a Python dictionary?
# import requests
# response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
# data = response.json() #retuns a dictionary
# print(data)
#
# .json() is used when the response content is in JSON format .internally it uses json.loads()
import json

# Q2: What is the difference between json.dumps() and json.loads()?
# json.dumps() = Serialization(convert python ->JSON String) - python object  -JSON String
# json.loads() = Deserialization(coverts JSON String ->python object) -JSON String  - Python object

# import json
# #serialization
#
# python_dict = {"name":"chandra","age":30}
# json_string = json.dumps(python_dict)
#
# #Deserialazation
# json_string1 = '{"name":"sekhar","age":24}'
# python_obj = json.loads(json_string1)
#
# # Q3: How do you handle nested JSON data in Python?
# # You can access nested values using chained keys/indexes
# response = {
#     "user":{
#         "id":1,
#         "profile":{
#             "name":"chandra",
#             "email":"mandla@gmail.com"
#         }
#     }
# }
# #access nested fields
# print(response['user']['profile']['email'])

# How do you safely handle missing keys in nested JSON?
# use .get() method to avoid KeyError
# email = response.get('user',{}).get('profile',{}).get('email','N/A')
#
# Q5: How do you parse a JSON array in Python?
# A JSON Array is converted to a python list
# import json
# json_array = '[{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]'
# data = json.loads(json_array)
#
# for user in data:
#     print(user['name'])

# Q6: How do you parse a list of objects in a JSON response?
# response = {
#     "users": [
#         {"id": 1, "name": "Alice"},
#         {"id": 2, "name": "Bob"}
#     ]
# }
# for user in response['users']:
#     print(f"User ID:{user['id']},Name:{user['name']}")

# Q7: What is the output type of response.json()?
# response.json() returns a python dictionary(or list if the top-level JSON is an array)

# Q8: How do you write a Python dictionary to a .json file?
# import json
# data = {"name":"chandra","age":30}
# with open('data.json','w') as f:
#     json.dump(data,f)

# Q9: How to read a .json file and convert it to a Python object?
# with open('data.json','r') as f:
#     data = json.load(f)
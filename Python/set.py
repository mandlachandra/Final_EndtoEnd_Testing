import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

#convert response to dictionary
response_dict = response.json()
print(type(response_dict))
print(response_dict)
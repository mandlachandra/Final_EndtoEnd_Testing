#how to convert json into python dictionary
import requests

#API url
url = "https://jsonplaceholder.typicode.com/posts/1"

#make get request
response = requests.get(url)

#convert json response to python dictionary
data = response.json()

print(type(data))
print(data)

#2nd method
#By using json.loads()
import json

#json string
json_string = '{"name":"chandra","age":30,"city":"hyd"}'

#convert json string into python dictionary
data1 = json.loads(json_string)
print(type(data1))
print(data1)
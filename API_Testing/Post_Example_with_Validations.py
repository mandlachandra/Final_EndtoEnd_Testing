import requests
import time
import json

from jsonschema import validate,ValidationError

#1.Define end point
url = "https://jsonplaceholder.typicode.com/posts"

#define headers
headers = {
    "Content-Type":"application/json"
}

#define payload
payload = {
    "title":"API Automation",
    "body":"This is sample post",
    "userid":102
}

#make the post request and capture the screen
start_time = time.time()
response = requests.post(url,headers=headers, json=payload)
end_time = time.time()
response_time = end_time-start_time

#convert response into dictionary
try:
    response_dict = response.json()
except ValueError:
    print("response is not valid")

#print response
print("response status code:",response.status_code)
# print("response body:,)


import requests
import time
import logging
from jsonschema import validate
import json

#configure logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s')

#url and payload
url = "https://reqres.in/api/users"
payload = {
    "name":"chandra",
    "job":"software"
}

#expected json schema for validation
response_schema = {
    "Type":"object",
    "poperties":{
        "name":{"type":"string"},
        "job":{"type":"string"},
        "id":{"type":"string"},
        "createAt":{"type":"string","format":"date-format"}
    },
    "required":["name","job","id","creatAt"]

}
#send post request
start_time = time.time()
response = requests.post(url,json=payload)
end_time = time.time()

#Log request and response
logging.info(f"Request URL: {url}")
logging.info(f"Request payload: {json.dumps(payload)}")
logging.info(f"Response Status Code: {response.status_code}")
logging.info(f"Response Headers: {response.headers}")
logging.info(f"Response Body: {response.text}")

#validations

#1.Status code
assert response.status_code == 201, f"Expected 201 but got {response.status_code}"

#2.Response Time
response_time = end_time-start_time
assert response_time <2, f"Response time is too high: {response_time} seconds"

#3.validate headers
assert response.headers["content-Type"] == "application/json; charset=utf-8",\
f"unexpected content-Type: {response.headers['Content-Type']}"

#4.validate Response Body keys
response_json = response.json()
assert response_json["name"]==payload["name"],"Name mismatch"
assert response_json["job"]==payload["job"], "job mismatch"
assert "id" in response_json,"ID not present in response"
assert "createAt" in response_json, "createAt not present in response"

#5.validate JSON Schema
validate(instance=response_json,schema=response_schema)

logging.info("All validations  passed successfully!")


#
#Post with Basic Auth
# import requests
# from requests.auth import HTTPBasicAuth
#
# url = "https://reqres.in/api/users"
# payload = {"name": "John", "role": "admin"}
#
# response = requests.post(url,json=payload,auth=HTTPBasicAuth("username","password"))
# print("status Code:",response.status_code)
# print("response:",response.json())

#post with bearer token
# import requests
#
# url = "https://reqres.in/api/users"
# payload = {"name": "John", "role": "admin"}
#
# headers = {
#     "Authorization":"Bearer your_access_token",
#     "content-type":"Application/json"
# }
#
# response = requests.post(url,json=payload,headers=headers)

import requests
import pytest
import json

# json_string = '{"name":"chandra","age":30,"city":"hyd"}'
# python_dict = {"name":"chandra sekhar mandla","age":30,"city":"hyd"}
#
# #convert json string into python dictionary
#
# data = json.loads(json_string)
# print(data)
#
# #convert python dictionary into json string
# json_string1 = json.dumps(python_dict)
# print(json_string1)

#How to send headers in a request?
# headers = {
#     'Authorization':'Beaer your_access_token'
# }
# response = requests.get("https://api.example.com/users",headers=headers)

#How do you send a POST request with JSON body?
# url = "https:api.example.com"
# data = {"name":"chandra"}
# response= requests.post(url,json=data)

# how do you handle Authentication in requests ?
# import requests
# from requests.auth import HTTPBasicAuth
#
# response = requests.get(url,auth=HTTPBasicAuth('user','pass'))

# How to extract json from a response
# response.json()

# How to validate a specific field in the json response
# assert response.json()['name']=='john'

# how do you print all headers in response
#print(response.headers)

# How do you handle timeouts in requests
# requests.get(url,timeout=10)

# def test_get_call():
#     response = requests.get()
#     assert response.status_code==200

# How do you parametrize API Tests in pytest ?
# @pytest.mark.parametrize('user_id',[1,2,3])
# def test_get_call(user_id):
#     response = requests.get(f"https://api.example.com/users/{user_id}")
#     assert response.status_code == 200
#
# # How do you setup/teardown in pytest for api testing ?
# use pytets.fixture to setup and teardown

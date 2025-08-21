#how to convert json into python dictionary
import pytest
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

#How to send headers in a request?

# headers = {'headers':'Bearer-token'}
# response = requests.get(url,headers=headers)

#How do you send a POST request with JSON body?
# data = {'name':'chandra'}
# response = requests.post(url,json=data)

# How do you send a GET request in Python?
# response = requests.get('https://api.example.com/users')
# print(response.status_code)

# how do you handle Authentication in requests ?
# from requests.auth import HTTPBasicAuth
# requests.get(url,auth=HTTPBasicAuth('user','pass'))

# How to extract json from a response
# response.json()

# how to assert response status code
# assert response.status_code==200

# How to validate a specific field in the json response
# assert response.json()['name']=='john'
# assert response.json()['age']==30

# how do you print all headers in response
# print(response.headers)

# How do you handle timeouts in requests
# requests.get(url,timeout=5)
# requests.get(url,timeout=10)
#
# How do you write a test case in pytest for api ?
# def test_get_call():
#     response = requests.get(url)
#     assert response.status_code == 200

# How do you parametrize API Tests in pytest ?
# @pytest.mark.parametrize("user_id",[1,2,3])
# def test_call(user_id):
#     response = requests.get(f"https://api.example.com/users/{user_id}")
#     assert response.status_code == 200

# How do you setup/teardown in pytest for api testing ?
# use pytest.fixture to setup baseurls,tokens etc.

# How to group api tests using markers ?
# @pytest.mark.smoke
# def test_api:
#     pass

# How to generate HTML Reports
# pytest --html= report.html

# How to validate JSON response with schema?
# from jsonschema import validate
# validate(instance=response.json(),schema=expected_schema)

# How to test file upload API using Python?
# files = {'file': open('data.csv', 'rb')}
# response = requests.post(url, files=files)
#
# How to send query parameters in request?
# requests.get(url,params={'page':2})
# requests.get(url,params={'page':4})

# How to chain requests (use response from one in another)?
# user_id = requests.get(url).json()['id']
# requests.get(f'{url}/{user_id}')
#
# How to capture response time?
# print(response.elapsed.total_seconds())
#
# How to retry failed requests?
# use urllib3.util.retry or tenacity

# What is the difference between Basic Auth and Bearer Token?
# Basic Auth  uses username/password, bearer token is usually Oauth based token
#
# How to pass OAuth2 token in request?
# headers = {'Authorization':'Bearer-token'}








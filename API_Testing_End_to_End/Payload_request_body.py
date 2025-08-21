# Q1: How do you pass a JSON payload from a dictionary in a POST request?
# You can use the json parameter in the requests.post() call to send a python dictionary as a json payload
# import requests
# payload = {"name":"chandra","age":"30"}
# response = requests.post("https://api.com/users",json=payload)
# import json
#
# This internally uses json.dumps(payload) and sets content-type to application/json

# Q2: How do you send a JSON payload by reading from a .json file?
# import json
# import requests
#
# with open('payload.json') as f:
#     data = json.load(f)
#
# response = requests.post("",json=data)

# Q3: What are fixtures in pytest and how can they be used for dynamic payloads?
#
# # conftest.py or test file
# import pytest
#
#
# @pytest.fixture
# def user_payload():
#     return {
#         "name": "User123",
#         "email": "user123@example.com"
#     }
#
#
# def test_create_user(user_payload):
#     response = requests.post("https://api.example.com/users", json=user_payload)
#     assert response.status_code == 201

# Q4: How can you make pytest fixtures dynamic with parameters?
#
#
# @pytest.fixture
# def user_payload(request):
#     return {
#         "name": request.param,
#         "email": f"{request.param}@example.com"
#     }
#
#
# @pytest.mark.parametrize("user_payload", ["UserA", "UserB"], indirect=True)
# def test_user_payload(user_payload):
#     response = requests.post("https://api.example.com/users", json=user_payload)
#     assert response.status_code == 201

# Q5: What is a Pydantic model and how is it used in API testing?
# Pydantic is a data validation library that uses python type hints to define and validate models
#
# from pydantic import BaseModel
#
# class User(BaseModel):
#     name: str
#     email: str
#
# user = User(name="Alice", email="alice@example.com")
# print(user.dict())  # Convert to dictionary
#
# response = requests.post("https://api.example.com/users", json=user.dict())

# Q6: What are the benefits of using Pydantic models for payloads?
# Type
# validation and auto - completion
#
# Cleaner and structured
# payload
# generation
#
# Default
# values, validators, and parsing
# nested
# models
#
# Better
# integration
# with FastAPI(backend)

# Q7: When would you use .data instead of .json in a request?
# Answer:
#
# Use .data when sending form data (application/x-www-form-urlencoded).
#
# Use .json for structured JSON payloads.
#
# Q8: Can
# you
# send
# a
# JSON
# payload
# using
# json.dumps()
# directly in a
# request?
# Answer:
# Yes, but
# you
# must
# also
# set
# the
# content - type
# manually.
#
# python
# Copy
# Edit
# import json
#
# headers = {'Content-Type': 'application/json'}
# requests.post(url, data=json.dumps(payload), headers=headers)

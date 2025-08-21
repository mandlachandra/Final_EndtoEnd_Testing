#required libraries
# pip install pytest requests

#Folder structure
# api_test_framework
# ->tests
# ---->test_users_api.py
# ->data
# ---->test_data_json
# ->utils
# ---->helper.py
# ->conftest.py
# ->requirements.txt
# ->pytest.ini

#Get Request
# import requests
#
# def test_get_users():
#
#     response = requests.get("https://reqres.in/api/users?page=2")
#     assert response.status_code ==200
#     assert response.json()["page"] == 2

#post request
import requests

# def test_create_user():
#
#     url= "https://reqres.in/api/users"
#     payload= {"name":"chandra","job":"software"}
#     headers ={
#         "Authorization":"Bearer YOUR_ACCESS_TOKEN",
#         "Content-Type":"application/json"
#     }
#     response = requests.post(url,json=payload,headers=headers)
#     assert response.status_code == 201
#     assert response.json()["name"] == "chandra"

#PUT and PATCH request
def test_update_user():

    payload = {"name":"sekhar","job":"business"}
    response = requests.put("https://reqres.in/api/users/2",json=payload)
    assert response.status_code ==200

#Delete request

def test_delete_user():

    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204

#Authentication
#Bearer-Token
def test_bearer_token_auth():

    headers = {
        "Authorization":"Bearer your_token_here"
    }
    response = requests.get("https://reqres.in/api/protected",headers=headers)
    assert response.status_code == 200

#BasicAuth
from requests.auth import HTTPBasicAuth
def test_basic_auth():

    response = requests.get("https://reqres.in/api",auth=HTTPBasicAuth('user','pass'))
    assert response.status_code==200

#Fixtures for reuse (conftest.py)
import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in.api"

def test_with_fixture(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200

#Assertions and JSON Path
def test_json_validation():
    response = requests.get("https://reqres.in/api/users/2")
    data =response.json()
    assert data["data"]["email"] =="mandlachandra2014@gmail.com"

#parameterization
import pytest

@pytest.mark.parametrize("name,job",[
    ("chandra","king"),
    ("sekhar","leader")
])
def test_create_user(name,job):
    payload = {"name":name,"job":job}
    response = requests.post("https://reqres.in/api/users",json=payload)
    assert response.status_code == 201

#logging Requests and response

def test_logging():
    payload = {"name":"chandra","job":"software"}
    response = requests.post("https://reqres.in/api/users",json=payload)

    print("Requests:",payload)
    print("Status_code:",response.status_code)
    print("Response body:",response.text)

    assert response.status_code ==201

#Extracting values

    def test_extract_token():
        response = requests.post("https://reqres.in/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        token = response.json().get("token")
        assert token is not None


#Negative testing

def test_login_invalid():
    payload = {"email":"wrong@email.com"}
    response = requests.post("https://reqres.in/api/login",json=payload)
    assert response.status_code ==400
    assert response.json()["error"]  == "missing password"

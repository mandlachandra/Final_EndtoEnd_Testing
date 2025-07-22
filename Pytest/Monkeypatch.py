#Monkeypatching means dynamically changing or replacing parts of your code at runtime(like functions,objects,environmental variables)
#In pytest you can use built-in monkeypatch fixture to:
#Replace functions or methods
#set or change environmental variables
#patch attributes or  modules for testing

#This is super useful when you want to
#Avoid calling external APIS during tests
#Replace file system/database calls
#Mock out behaviour without external libraries

#Replace a function dynamically

def get_username():
    #imagine this fetches from DB
    return "real_users"

import app
import pytest
def test_get_username(monkeypatch):
    #Replace get_username with a lambda returning fake user
    monkeypatch.setattr(app,"get_username",lambda:"fake_user")

    assert app.get_username()=="fake_user"

#monkeypatch an environment variable
import os

def get_env():
    return os.getenv("My_env","default")

def test_get_env(monkeypatch):
    monkeypatch.setenv("My_env","test_value")
    assert app.get_env() == "test_value"


#Monkeypatch a method in a class
class APIClient:
    def fetch_data(self):
        # Pretend this hits an external API
        return {"status": "real data"}

import app

def test_fetch_data(monkeypatch):
    def fake_fetch(self):
        return {"status": "mocked data"}

    monkeypatch.setattr(app.APIClient, "fetch_data", fake_fetch)

    client = app.APIClient()
    assert client.fetch_data() == {"status": "mocked data"}

#Monkeypatch a dictionary key
settings = {"mode":"production"}

def test_patch_dict(monkeypatch):
    monkeypatch.setitem(app.settings,"mode","testing")
    assert app.settings["mode"]== "testing"

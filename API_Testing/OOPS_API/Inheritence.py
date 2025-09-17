#For Michaels APIS(Search,Cart,Checkout) all requests share:
# ->Base url
# ->Authentication headers
# you can put them in BaseAPI class

#base_api.py

import requests

class BaseAPI:
    BASE_URL = "https://api.michaels.com"

    def get(self,endpoint,params= None):
        return requests.get(f"{self.BASE_URL}{endpoint}",params=params)

    def post(self,endpoints,data=None):
        return requests.post(f"{self.BASE_URL}{endpoints}",json=data)

#search_api.py

#from base_api import BaseAPI
class SearchAPI(BaseAPI):

    def search(self,query):
        return self.get("/search",{"q":query})

    

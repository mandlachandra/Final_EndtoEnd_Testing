# Encapsulation means bundling data (variables) and methods(functions) together in a class
# while restricting direct access to some parts.

# Encapsulate base URL  and headers inside an API Client

import requests

class MichaelsAPI:

    __BASE_URL = "https://michaels.com"
    __HEADERS = {"Authorization":"Bearer <token>"}

    def search(self,query):
        return requests.get(f"{self.__BASE_URL}/search",
                            params={"q":query},
                            headers = self.__HEADERS)

#Tests don't need to know base url or headers
#just call api.search("yarn")


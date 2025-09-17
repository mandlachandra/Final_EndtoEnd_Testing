from abc import ABC, abstractmethod
import requests

class BaseAPI(ABC):

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get(self, endpoint, params=None):
        pass

    @abstractmethod
    def post(self, endpoint, data=None):
        pass


class MichaelsAPI(BaseAPI):

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data)

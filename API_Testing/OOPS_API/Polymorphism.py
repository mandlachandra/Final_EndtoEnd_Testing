#In Michaels different Apis (SearchAPI,CartAPI,CheckoutAPI) may implement a common
#call_api() method but different logic

class BaseAPI:
    def call_api(self):
        raise NotImplementedError

class SearchAPI(BaseAPI):

    def call_api(self):
        return "search api response"

class CartAPI(BaseAPI):
    def call_api(self):
        return "cart api response"

class CheckoutAPI(BaseAPI):

    def call_api(self):
        return "checkout api response"

#polymorphism in action
apis = [SearchAPI(),CartAPI(),CheckoutAPI()]
for api in apis:
    print(api.call_api())
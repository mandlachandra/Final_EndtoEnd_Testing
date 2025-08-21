#How do you handle authentication is API
#Basic Authentication
# Uses username and password encoded in Base64
# sent into the Authorization Header
# Not secure alone - should be used over HTTPS only
# import requests
# from requests.auth import HTTPBasicAuth
#
# response = requests.get("https://example.com/data",auth=HTTPBasicAuth('username','password'))
# print(response.status_code)

#Bearer Token
# Uses a token which is passed in the Authorization Header
# More secure and scalable than Basic Auth
# Often used with Oauth 2.0 flow

import requests

headers = {
    "Authorization":"Bearer your access_Token"
}
response = requests.get("https://example.com/data",headers= headers)

#API Key
# A simple static key passed in headers or query parameters
# Less secure if exposed but commonly used for internal or less sensitive APIs

headers = {
    'x-api-key':"your_api_key"
}
response = requests.get('https://api.example.com/data',headers=headers)

#session based Authentication
# common in web applications
# After login a session cookie is returned and reused in subsequent requests
session = requests.Session()
session.post("https://api.example.com/login",data = {"user":"abc","pass":"zxp"})
response = session.get("https://api.example.com/data")





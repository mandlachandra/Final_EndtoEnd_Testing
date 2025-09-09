import json


import requests

#How to send headers in a request?

#How do you send a POST request with JSON body?

# How do you send a GET request in Python?

# how do you handle Authentication in requests ?

# How to extract json from a response

# How to validate a specific field in the json response

# how do you print all headers in response

# How do you handle timeouts in requests

# How do you write a test case in pytest for api ?

# How do you parametrize API Tests in pytest ?

# How do you setup/teardown in pytest for api testing ?


# How to group api tests using markers ?


# How to generate HTML Reports

# How to validate JSON response with schema?

# How to test file upload API using Python?

# How to send query parameters in request?

# How to chain requests (use response from one in another)?

# How to capture response time?

# How to retry failed requests?

# What is the difference between Basic Auth and Bearer Token?

# How to pass OAuth2 token in request?

import requests

# base_url = "https://jsonplaceholder.typicode.com/users"
# user_id = 5
#
# response = requests.get(f"{base_url}/{user_id}")
# print("status_code:",response.status_code)
# print("response:",response.json())



#query parameters
url = "https://jsonplaceholder.typicode.com/posts"
#query params dictionary
params = {
    "user_id":1,
    "id":5
}

response = requests.get(url,params=params)
print(f"final url:",response.url)
print("status:",response.status_code)
print("response:",response.json())

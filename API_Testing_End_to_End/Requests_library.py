#Q1: How do you send a GET request using Python?

import requests
response = requests.get("https://reqres.in/com/users")
print(response.status_code)
print(response.json())

#Q2: How do you send a POST request with JSON payload?
payload = {"name":"chandra","job":"software"}
response= requests.post("https://api.example.com/users",json=payload)

# Q3: What is the difference between PUT and DELETE methods?
# PUT = updates/replaces a resources
# DELETE = removes the resource from the server

# PUT
# requests.put("https://api.example.com/users/1",json={"name":"updated"})
#
# delete
# requests.delete("https://api.example.com/users/1")

# Q4: How do you pass query parameters in a GET request?
# params ={"pages":2,"limit":10}
# response = requests.get("https://example.com/users",params=params)

# Q5: How do you use path parameters in requests?
# user_id =123
# url = f"https://example.com/users/{user_id}"
# response = requests.get(url)

# Q6: How do you pass custom headers in a request?
# headers = {"Authorization":"Bearer <token>","Content-Type":"application/json"}
# response = requests.get("https://example.com/profile",headers=headers)

# Q7: How do you send cookies with a request?
# cookies = {"session_id":"abcd1234"}
# response = requests.get("https://example.com/dashboard",cookies=cookies)

# Q8: What is the difference between data and json parameters in a POST request?
# json = sends the payload as JSON with Content-Type : application/json.
# data = sends from data as application/x-www-form-urlencoded(default)

#JSON Payload
# requests.post(url,json={"name":"john"})
#
# #from data
# requests.post(url, data={"name":"chandra"})

# Q10: How do you send form-data in a POST request?
# form_data = {'username':'admin','password':'123456'}
# requests.post(url,data=form_data)

# Q11: How do you upload a file using Python requests?
# files = {'file':open('report.pdf','rb')}
# response = requests.post("https://example.com/upload",files=files)

# How do you extract JSON data from the response?
# response.json()
#
# Q14: What is the use of response.text?
# it returns a raw text content of the response body as a string
# html_content = response.text
#
# Q15: How to access headers in the response?
# print(response.headers)
# print(response.headers['Content-Type'])

# Q16: What if .json() throws an error?
# If the response is not valid JSON Format , response.json() will raise JSONDecodeError
# you can check content-type or fallback to response.text


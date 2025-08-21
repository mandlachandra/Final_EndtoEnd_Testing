import json
data = '{"k1":"value1","k2":"value2"}' #dictionary in the form of string
json_result = json.loads(data)
print(json_result)
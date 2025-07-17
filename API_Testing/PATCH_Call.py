import requests
import json
from jsonschema import validate
import logging
import time

# 🔥 Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# ✅ API URL and Payload
url = "https://reqres.in/api/users/2"
payload = {
    "name": "morpheus",
    "job": "zion leader"
}

# ✅ Expected JSON Schema
response_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["name", "job", "updatedAt"]
}

# ✅ Send PATCH Request
start_time = time.time()
response = requests.patch(url, json=payload)
end_time = time.time()

# ✅ Log Request and Response
logging.info(f"Request URL: {url}")
logging.info(f"Request Payload: {json.dumps(payload)}")
logging.info(f"Response Status Code: {response.status_code}")
logging.info(f"Response Headers: {response.headers}")
logging.info(f"Response Body: {response.text}")

# ✅ Validations
# 1. Status Code
assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

# 2. Response Time (< 2 seconds)
response_time = end_time - start_time
assert response_time < 2, f"Response time too high: {response_time:.2f} seconds"

# 3. Headers
assert "application/json" in response.headers["Content-Type"], \
    f"Unexpected Content-Type: {response.headers['Content-Type']}"

# 4. Response Body Content
response_json = response.json()
assert response_json["name"] == payload["name"], f"Expected name '{payload['name']}' but got '{response_json['name']}'"
assert response_json["job"] == payload["job"], f"Expected job '{payload['job']}' but got '{response_json['job']}'"
assert "updatedAt" in response_json, "'updatedAt' not present in response"

# 5. JSON Schema Validation
validate(instance=response_json, schema=response_schema)

logging.info("✅ All validations passed successfully!")

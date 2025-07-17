import requests
import json
from jsonschema import validate
import logging
import time

# 🔥 Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# ✅ URL
url = "https://reqres.in/api/users?page=2"

# ✅ Expected JSON Schema for validation
response_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string", "format": "email"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string", "format": "uri"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"]
}

# ✅ Send GET Request
start_time = time.time()
response = requests.get(url)
end_time = time.time()

# ✅ Log Request and Response
logging.info(f"Request URL: {url}")
logging.info(f"Response Status Code: {response.status_code}")
logging.info(f"Response Headers: {response.headers}")
logging.info(f"Response Body: {response.text}")

# ✅ Validations
# 1. Status Code
assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

# 2. Response Time (should be < 2 seconds)
response_time = end_time - start_time
assert response_time < 2, f"Response time too high: {response_time:.2f} seconds"

# 3. Validate Headers
assert response.headers["Content-Type"] == "application/json; charset=utf-8", \
    f"Unexpected Content-Type: {response.headers['Content-Type']}"

# 4. Validate Response Body Content
response_json = response.json()
assert response_json["page"] == 2, f"Expected page=2 but got page={response_json['page']}"
assert response_json["total_pages"] >= 1, "total_pages is less than 1"

# Check first user’s email format
first_user_email = response_json["data"][0]["email"]
assert "@" in first_user_email, "First user's email is invalid"

# 5. Validate JSON Schema
validate(instance=response_json, schema=response_schema)

logging.info("✅ All validations passed successfully!")

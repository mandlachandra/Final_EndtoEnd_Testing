import requests
import logging
import time

# 🔥 Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# ✅ API URL
url = "https://reqres.in/api/users/2"

# ✅ Send DELETE Request
start_time = time.time()
response = requests.delete(url)
end_time = time.time()

# ✅ Log Request and Response
logging.info(f"Request URL: {url}")
logging.info(f"Response Status Code: {response.status_code}")
logging.info(f"Response Headers: {response.headers}")
logging.info(f"Response Body: '{response.text}'")  # Should be empty

# ✅ Validations
# 1. Status Code
assert response.status_code == 204, f"Expected 204 but got {response.status_code}"

# 2. Response Time (< 2 seconds)
response_time = end_time - start_time
assert response_time < 2, f"Response time too high: {response_time:.2f} seconds"

# 3. Headers Validation
assert "Content-Type" in response.headers or "content-type" in response.headers, \
    "Content-Type header missing"

# 4. Response Body should be empty
assert response.text == '', f"Expected empty body but got: {response.text}"

logging.info("✅ All validations passed successfully!")

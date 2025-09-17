import requests
from selenium import webdriver

# Initialize browser
driver = webdriver.Chrome()
driver.get("https://example.com")

# Collect all <a> tags
links = driver.find_elements("tag name", "a")

for link in links:
    url = link.get_attribute("href")
    if url is None or url.strip() == "":
        print("Empty or None link found")
        continue

    try:
        response = requests.head(url, timeout=5)  # HEAD request is faster
        if response.status_code >= 400:
            print(f"❌ Broken link: {url} -> Status: {response.status_code}")
        else:
            print(f"✅ Valid link: {url} -> Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Exception for {url}: {e}")

driver.quit()

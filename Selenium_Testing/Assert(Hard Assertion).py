# If the condition fails, the test stops immediately.
#
# It’s part of Python’s built-in assert statement or pytest.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.michaels.com")

# Get title
title = driver.title

# Hard assertion
assert "Michaels" in title, "Title does not contain 'Michaels'"

print("✅ This will only run if assertion passes")

driver.quit()


# Even if the condition fails, the test continues execution.
#
# Python doesn’t have a direct verify, but we can achieve it using try-except or pytest plugins like softest or pytest-check.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.michaels.com")

errors = []

try:
    assert "Crafts" in driver.title
except AssertionError:
    errors.append("❌ Title verification failed")

try:
    element = driver.find_element(By.ID, "search-input")
    assert element.is_displayed()
except AssertionError:
    errors.append("❌ Search box is not displayed")

if errors:
    print("\n".join(errors))

print("✅ Test continued execution even after failures")

driver.quit()

#3. Using pytest-check (soft assertions)

# pip install pytest-check
#
# import pytest_check as check
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_soft_assert():
#     driver = webdriver.Chrome()
#     driver.get("https://www.michaels.com")
#
#     check.is_in("Crafts", driver.title)  # will not stop execution
#     check.is_true(driver.find_element(By.ID, "search-input").is_displayed())
#
#     driver.quit()

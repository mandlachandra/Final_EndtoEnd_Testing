# 2. Explain the structure of your Selenium framework.
# tests - All test cases
# pages - page object classes
# utilities - common methods(e.g , waits,Excel utils)
# config - congig files(urls,credentials, browsers)
# logs - logging mechanism
# reports - Allure or HTML Reports
# conftest.py -For setup and Teardown (pytest)
# requirements.txt = Dependency management
# pytest.ini/tox.ini = Pytest configurations

# What is Page Object Model (POM)? Why is it used?
# POM is a design pattern where:
# Each web page is represented as a class
# Locators and methods are encapsulated
# It promotes reusability , readability and maintainability
#
# class LoginPage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def enter_username(self,username):
#         self.driver.find_element(By.ID,"username").send_keys(username)
#
#     def click_login(self):
#         self.driver.find_element(By.ID,'login').click()

# How do you manage test data in your framework?
# I use
# Excel/CSV/JSON files (for Data-Driven testing)
# Read using openpyxl or pandas
# For BDD I use Scenario outlines with examples table

# How do you handle configurations like URL, browser, credentials?
# I use .ini ,.yaml,.json files
# Example (config.json)
# {
#     "base_url":"https://example.com",
#     "browser":"chrome",
#     "username":"admin"
# }
# import json
# config = json.load(open("config/config.json"))

# How do you implement logging in your framework?
# import logging
# logging.basicConfig(filename="logs/test.log",level=logging.INFO)
# logging.info("Test started")

# How do you implement exception handling in your tests?
# I wrap selenium actions in try-except blocks
# log or take screenshots on exceptions
# use custom exception classes for specific validations
#
# try:
#     driver.find_element(By.ID,"butotn").click()
# except Exception as e:
#     logging.error("Login button failed",exc_info=True)

# How do you manage parallel execution in your framework?
# pytest -n 4

# How do you integrate your framework with Jenkins or CI tools?

#What challenges did you face in Selenium automation and how did you overcome them?
import selenium.common.exceptions

#dynamic Xpath issues = Used robust locators
# Flaky tests due to sync issues = Used explicit waits
# cross-browser compatability = used Selenium Grid /Browser stack
# Test data management = Externalize data using Excel/DB_Testing
# Parallel execution failures = used thread-safe webdriver instances
# CI/CD pipeline failures = Added retry mechanisms , dockerized browsers

#dynamic Xpath issues = Used robust locators
# The element attributes(id,name,class etc) keep changing every time once page loads
# for example , IDs like id = "username_1234",id="username_6578" changes on refresh
# if we write direct xpath it will fails
# driver.find_element(By.XPATH,"//input[@id='username_1234']")

# How to solve this ? use robust locators
# Instead of relying on chaning IDs or attributes, use stable parts like
# contains()
# starts-with()
# text() or normalize-space()
# following-sibling, preceding-sibling , parent:: etc
#
# #using contains
# #bad
# driver.find_element(By.XPATH,"//input[@id='user_123']")
#
# #Good
# driver.find_element(By.XPATH,"//input[contains(@id,'user')]")
#
# #using starts-with()
# #bad
# driver.find_element(By.XPATH,"//button[@id='loginbutton_987']")
#
# #good
# driver.find_element(By.XPATH,"//button[starts-with(@id,'loginbutton)]")
#
# #with normalize-space
# driver.find_element(By.XPATH,"//button[normalize-space(text())='login']")
#
# #Using Relative XPath (parent/child/sibling)
# # Example: Input box next to label "Username"
# driver.find_element(By.XPATH, "//label[text()='Username']/following-sibling::input")
#
# Multiple Attributes for Robustness
#     # Instead of only ID, combine stable attributes
#     driver.find_element(By.XPATH, "//input[@type='text' and contains(@name,'user')]")

#>......................................
# Flaky tests due to sync issues = Used explicit waits
#What are Flaky Tests due to Sync Issues?
# A flaky test is the one that sometimes passes and sometimes fails without any code changes
# In selenium this usually happens because the script runs faster than the application
#
# Example of flaky code:
# driver.get("https://example.com")
# driver.find_element(By.ID,"loginbtn").click() #may fail if button takes time to load
#
# #Error you might see:
# selenium.common.exceptions.NoSuchElementException
# selenium.common.exceptions.ElementNotInteractableException

#Solution
# Instead of blindly clicking/fetching, we will wait until the condition is met.
# selenium provides webdriverwait + Expected condition

#Example 1: Wait for Element to be Clickable
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver,10) #max wait time 10 second
# login_button = wait.until(EC.element_to_be_clickable(By.ID,"loginbutton")))
# login_button.click()
#
# #Example 2: Wait for Visibility of Element
# username = wait.until(EC.visibility_of_element_located(By.NAME,"username")))
# username.send_keys("admin")
#
# #Example 3: Wait for Presence of Element in DOM
# element = wait.until(EC.presence_of_element_located(By.XPATH,""))
#
# #Example 4: Wait for Alert
# alert = wait.until(EC.alert_is_present())
# print(alert.text)
# alert.accept()










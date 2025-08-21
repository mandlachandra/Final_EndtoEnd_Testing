# #1. How do you handle dynamic elements in Selenium?
# # Dynamic elements often have IDs or attributes that change ,we handle them by:
# # Using stable Xpath/CSS based on surrounding text or structure
# # driver.find_element(By.XPATH,"//input[contains(@id,'username')]")
# # Using starts-with(),contains(), or relative Xpath
#
# # 2. How do you handle waits in Selenium?
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # driver = webdriver.Chrome()
# # # wait = WebDriverWait(driver,10)
# # # element = wait.until(EC.presence_of_element_located(By.ID,"username")))
# # #  why use:
# # # Implicit wait = for general waits across driver
# # driver.implicitly_wait(10)
#
# # driver.implicitly_wait(10)
# #
# # wait = WebDriverWait(driver,10).until(EC.presence_of_element_located)
# #
# # #Explicit Wait = For specifc condtions like visibility or clickable
# # wait = WebDriverWait(driver,10)
# # element = wait.until(EC.presence_of_element_located(By.XPATH,''))
# #
# # #Fluent Wait = Custom polling interval + Exception handling
#
# #how do you handle dropdowns in selenium ?
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.maximize_window()
# time.sleep(4)
#
# dropdown = driver.find_element(By.ID,"Skills")
# select = Select(dropdown)
#
# select.select_by_visible_text("C")
# time.sleep(2)
# print("Success")
#

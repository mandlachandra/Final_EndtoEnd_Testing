# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# time.sleep()
#
# #implicit wait
# driver.implicitly_wait(10)
#
# #Explicit wait
# wait = WebDriverWait(driver,10)
# element = wait.until(EC.presence_of_element_located((By.ID,"login")))
# element.click()
#
# #Fluent wait
# wait = WebDriverWait(driver,timeout=15,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
# element = wait.until(EC.presence_of_element_located((By.ID,"login")))
# element.click()
#
# #wait = WebDriverWit(driver,timeout=15,poll_frequency=2,ignored_exceptions= [NoSuchElementException])
#
#

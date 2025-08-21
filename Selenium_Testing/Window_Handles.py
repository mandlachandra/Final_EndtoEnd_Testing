# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
# time.sleep(2)
#
# parent_handle = driver.current_window_handle
# print("parent handle:",parent_handle)
#
# driver.find_element(By.ID,'tabButton').click()
# time.sleep(4)
#
# handles = driver.window_handles
# print("All handles:",handles)
#
# for handle in handles:
#     if handle!=parent_handle:
#         driver.switch_to.window(handle)
#         print("child window:",driver.title)
#         driver.close()
#
# driver.switch_to.window(parent_handle)
# print("Back to parent title:",driver.title)
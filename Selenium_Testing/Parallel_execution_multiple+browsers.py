# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# import threading
# import time
#
# #OrangeHrm Login function
# def orangehrm_login(browser_name):
#     print(f"[{browser_name}] starting....")
#
#     driver = None
#
#     try:
#         if browser_name == "chrome":
#             driver = webdriver.Chrome(service=ChromeService())
#         elif browser_name == "firefox":
#             driver = webdriver.Firefox(service=FirefoxService())
#         elif browser_name == "edge":
#             driver = webdriver.Edge(service=EdgeService())
#         else:
#             print(f"[{browser_name}] unsupported browser:")
#             return
#
#         driver.maximize_window()
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#
#         #Enter username
#         driver.find_element(By.NAME,"username").send_keys("Admin")
#
#         #Enter password
#         driver.find_element(By.NAME,"password").send_keys("admin123")
#
#         #click login button
#         driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
#         #wait for dashboard
#         time.sleep(3)
#         if "dashboard" in driver.current_url.lower():
#             print(f"[{browser_name}] login successfull")
#         else:
#             print(f"[{browser_name}] login failed")
#
#     except Exception as e:
#         print(f"[{browser_name}] Exception occurred: {e}")
#
#     finally:
#         time.sleep(5)
#         if driver:
#             driver.quit()
#
#         print(f"[{browser_name}] closed")
#
# #list of browsers to run
# browsers = ["chrome","firefox","edge"]
#
# #create a thread for each browser
# threads = []
#
# for browser in browsers:
#     t = threading.Thread(target=orangehrm_login,args=(browser,))
#     threads.append(t)
#     t.start()
#
# #wait for all threads to finish
# for t in threads:
#     t.join()
#
# print("All browsers executed in parallel.")

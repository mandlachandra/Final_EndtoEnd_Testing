# #Best practice to handle AJAX calls in selenium(python)
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as E
# driver = webdriver.Chrome()
#
# # 1.use Explicit Waits(Webdriver wait)
# # Instead of time.sleep(), always use explicit wait for all conditions
#
# wait = WebDriverWait(driver,10)
# # search_box = driver.find_element(By.ID,"search-input")
# # search_box.send_keys("yarn")
# # #wait until results are visible
# #results = wait.until(EC.presence_of_all_elements_located(By.XPATH,"//div[@class='search-results']//li")))
# # print(f"found {len(results)} results")
#
#
# #2.Wait for element to become clickable/visible
# button = wait.until(EC.element_to_be_clickable((By.ID,"submit-button")))
# button.click()
#
# #3.wait for invisibility of loader/spinner
# wait.until(EC.invisibility_of_element_located(By.CLASS_NAME,"loading-spinner")))
#
# #4.wait for text or attribute change
# wait.until(EC.text_to_be_present_in _element((By.ID,"status"),"completed"))
#
# #5.Custom Waits (Polling until AJAX is done)
# # Works if app uses jQuery
# wait.until(lambda d: d.execute_script("return jQuery.active == 0"))
# wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

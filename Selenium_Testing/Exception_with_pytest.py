# import pytest
# from selenium.common.exceptions import NoSuchElementException
#
# # def test_invalid_locator(driver):
# #     with pytest.raises(NoSuchElementException):
# #         driver.find_element("id","non_existent_element")
#
# def test_invalid_locator(driver):
#     with pytest.raises(NoSuchElementException):
#         driver.find_element("id","")
#
# #How do you handle stale element exceptions?
# #causes = DOM refresh/ page reload
#
# # element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"username"))
# # element.click()
#
# #How do you handle Shadow DOM elements in Selenium Python?
# #
# # shadow_root = driver.execute_script("return arguments[0].shadowRoot", host_element)
# # element = shadow_root.find_element(By.CSS_SELECTOR, "#shadowId")
#
# # #What challenges did you face in Selenium automation and how did you overcome them?
# #
# # #dynamic Xpath issues = Used robust locators
# # Flaky tests due to sync issues = Used explicit waits
# # cross-browser compatability = used Selenium Grid /Browser stack
# # Test data management = Externalize data using Excel/DB_Testing
# # Parallel execution failures = used thread-safe webdriver instances
# # CI/CD pipeline failures = Added retry mechanisms , dockerized browsers
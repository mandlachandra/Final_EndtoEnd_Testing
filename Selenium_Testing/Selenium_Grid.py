# # In Michaels project we had a requirement to validate our e-commerce application across multiple browsers
# # like chrome,firefox and edge, since a large user base was spread across thes
# # initially we were executing tests sequentially on our local machine which was very slow and not scalable
# # To address this i implemented Selenium Grid for distributed and parallel execution
# #
# # ->I set up a hub on a central server and registered multiple Nodes(Chrome,fireforx and edge)
# # running on different virtual machines
# # ->We integreted this with our Pytest framework so that based on the browser parameter the test cases
# # would dynamically pick the right node from the grid
# #
# # Ex:
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# def get_driver(browser_name):
#     grid_url = "http://hub.michaels.com:4444/wb/hub"
#     capabilities = {"browserName":browser_name}
#     return webdriver.Remote(command_executor=grid_url,
#                             desired_capabilities=capabilities)
#
# def test_login():
#     driver = get_driver("chrome") #could be firefor or edge
#     driver.get("https://www.michaels.com")
#     assert "Michaels" in driver.title
#     driver.quit()
#
# # #using Grid we achieved parallel execution across diferent browsers and OS combinations which
# # reduced execution time drastically (from 3 hours sequentially to under 1 hour in parallel)
# # ->Later we connected Selenium Grid with Jenkins pipeline so that every build triggered cross browser
# # test execution automatically
# #
# # ->This helped us ensure cross browser compatability and catch browser specific UI bugs early
# # improving product quality.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

# Grid Hub URL
GRID_URL = "http://localhost:4444/wd/hub"

# Browsers to test
browsers = ["chrome", "firefox"]


@pytest.mark.parametrize("browser", browsers)
def test_orangehrm_login(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError("Browser not supported!")

    driver = webdriver.Remote(command_executor=GRID_URL, options=options)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()

        # Perform Login
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()

        # Assertion: Check dashboard
        assert "dashboard" in driver.current_url.lower(), f"Login failed in {browser}"
        print(f"✅ Login test passed in {browser}")

    finally:
        driver.quit()

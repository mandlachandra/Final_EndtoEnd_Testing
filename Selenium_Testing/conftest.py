#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# import threading
# import time
#
# # ✅ OrangeHRM login function
# def orangehrm_login(browser_name):
#     print(f"[{browser_name}] Starting...")
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
#             print(f"[{browser_name}] Unsupported browser!")
#             return
#
#         driver.maximize_window()
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#
#         # Enter Username
#         driver.find_element(By.NAME, "username").send_keys("Admin")
#
#         # Enter Password
#         driver.find_element(By.NAME, "password").send_keys("admin123")
#
#         # Click Login Button
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#         # Wait for Dashboard
#         time.sleep(3)
#         if "dashboard" in driver.current_url.lower():
#             print(f"[{browser_name}] ✅ Login successful!")
#         else:
#             print(f"[{browser_name}] ❌ Login failed!")
#
#     except Exception as e:
#         print(f"[{browser_name}] ❌ Exception occurred: {e}")
#
#     finally:
#         time.sleep(5)  # Keep browser open for 5 sec
#         if driver:
#             driver.quit()
#         print(f"[{browser_name}] Closed.")
#
# # ✅ List of browsers to run
# browsers = ["chrome", "firefox", "edge"]
#
# # ✅ Create a thread for each browser
# threads = []
#
# for browser in browsers:
#     t = threading.Thread(target=orangehrm_login, args=(browser,))
#     threads.append(t)
#     t.start()
#
# # ✅ Wait for all threads to finish
# for t in threads:
#     t.join()
#
# print("🎯 All browsers executed in parallel.")
#

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#Add custom CLI options

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action = "store",
        default = "chrome",
        help = "Browser to run tests : chrome,firefox,edge"
    )
    parser.addoption(
        "--env",
        action = "store",
        default = "qa",
        help = "Environment to test: qa,uat,stage,prod"
    )
    parser.addoption(
        "--remote",
        action= "store_true",
        help= "run tests on selenium grid (if set) else local"

    )
    parser.addoption(
        "--grid_url",
        action = "store",
        default = "http://localhost:4444/wd/hub",
        help = "Selenium Grid Hub URL"
    )

#return base url form env

@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.get_option("--env")
    urls = {
        "qa":"https://qa.michaels.com",
        "uat":"https://uat.michaels.com",
        "stage":"https://stage.michaels.com",
        "prod":"https://www.michaels.com"
    }
    if env not in urls:
        raise pytest.UsageError(" ")
    return urls[env]

#driver initialization
@pytest.fixture(scope="function")
def driver(request,base_url):
    browser = request.config.get_option("--browser").lower()
    remote = request.config.get_option("--remote")
    grid_url  = request.config.get_option("--grid-url")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_argument("--headless") #enabled if needed

    elif browser == "firefox":
        options=FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height-1080")
    else:
        raise pytest.UsageError(f"unsupported browser '{browser}'")

    if remote : #run on selenium grid
        if browser == "chrome":
            driver = webdriver.Remote(command_executot=grid_url,options=options)
        elif browser == "firefox":
            driver=  webdriver.Remote(command_executor=grid_url,options=options)

    else: #run locally
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            driver = webdriver.firefox(options=options)

    driver.get(base_url)
    yield
    driver.quit()

#Example test using this conftest
def test_homepage_title(driver,base_url):
    assert "michaels" in driver.title

# how to run
# Local chrome on QA
# pytest -v --browser=chrome --env=qa
#
# local firefox on staging
# pytest -v --browser=firefox --env=staging
#
# remote chrome on selenium grid
# pytest -v --browser=chrome --env=qa --remote --grid_url="http://<GRID_IP>:4444/wd/hub"


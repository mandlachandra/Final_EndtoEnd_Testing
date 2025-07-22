import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome()
def get_browser(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"unsupported browser: {browser_name}")

@pytest.fixture(params=["chrome","firefox"])
def driver(request):
    print(f"\n launching {request.param} browser....")
    driver = get_driver(request.param)
    driver.maximize_window()
    yield driver
    print(|\f"\nclosing {request.param} browser....")
    driver.quit()
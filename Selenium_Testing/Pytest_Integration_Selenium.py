#you can use fixtures to handle browser setup/deardown automatically
#you can parametrize browsers(chrome,firefox,edge)
#you can get parallel execution easily with pytest-xdist
#your tests are modular,reusable and clean

# #1.Install dependencies
# pip install
# selenium
# pytest
# pytest-xdist
#
# pip install webdriver_manager

#step 2 : create fixture for browser setup
#initialize webdriver
#yields it to tests
#Quit browser after test

#conftest.py(browser setup)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    print("Launching browser....")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print("closing browser....")
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_bing_title(driver):
    driver.get("https://bing.com")
    assert "Bing" in driver.title

    


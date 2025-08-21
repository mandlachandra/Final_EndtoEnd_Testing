#1.Pytest installation and setup
#pip install pytest selenium
import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_login_valid():
#     driver = webdriver.Chrome()
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.find_element(By.ID,"txtusername").send_keys("admin")
#     driver.find_element(By.ID,"txtpassword").send_keys("admin123")
#     driver.find_element(By.ID,"btnlogin").click()
#     assert "dashboard" in driver.current_url.lower()
#     driver.quit()

#pytest -v

#Fixtures (Setup & Teardown for Selenium)
# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def setup_browser():
#     driver= webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# def test_google_title(setup_browser):
#     setup_browser.get("https://www.google.com")
#     assert "Google" in setup_browser.title

#4. Fixture Scope
#Fixtures can run at function, class,module or session level
# @pytest.fixture(scope="session")
# def setup_session():
#     print("\n>>seetup for session")
#     yield
#     print("\n>>Teardwon for session")

#Parameterization
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.mark.parametrize("username,password",[("Admin","admi123"),
#                                               ("Wronguser","wrongpass")])
#
# def test_login(browser,username,password):
#     browser.get("https://opensource-demo.orangehrmlive.com/")
#     browser.find_element(By.ID,"txtusername").send_keys(username)
#     browser.find_element(By.ID,"txtpassword").send_keys(password)
#     browser.find_element(By.ID,"btnlogin").click()

#Markers(Smoke,regression)

import pytest

@pytest.mark.smoke
def test_smoke(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

@pytest.mark.regression
def test_regressiom(driver):
    driver.get("https://www.google.com")
    assert "Bing" in driver.title

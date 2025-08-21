# # from pytest_bdd import scenarios, given, when, then,parsers
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import pytest
# # import time
#
# from pytest_bdd import scenarios, given, when, then, parsers
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
# import time
#
# # === Scenarios ===
# scenarios('orangehrm.feature')
#
#
# # === Step Definitions ===
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()  # Or Firefox/Edge
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# @given('the user launches the OrangeHRM login page', target_fixture='browser')
# def step_launch_browser(browser):
#     browser.get("https://opensource-demo.orangehrmlive.com/")
#     return browser
#
#
# @when(parsers.cfparse('the user enters username "{username}" and password "{password}"'))
# def step_enter_credentials(browser, username, password):
#     browser.find_element(By.NAME, "username").send_keys(username)
#     browser.find_element(By.NAME, "password").send_keys(password)
#
#
# @when('clicks on the login button')
# def step_click_login(browser):
#     browser.find_element(By.XPATH, "//button[@type='submit']").click()
#
#
# @then('the user should see the OrangeHRM dashboard')
# def step_verify_dashboard(browser):
#     time.sleep(3)  # Wait for page load
#     assert "dashboard" in browser.current_url.lower(), "Login failed or Dashboard not found"

# import psutil
# import time
#
# for _ in range(10):  # Monitor for 10 intervals
#     print(f"CPU: {psutil.cpu_percent()}%")
#     print(f"Memory: {psutil.virtual_memory().percent}%")
#     time.sleep(1)

# from behave import given, when, then
#
# @given('the user is on the login page')
# def step_impl(context):
#     print("User is on login page")
#
# @when('they enter valid username and password')
# def step_impl(context):
#     print("Entered username and password")
#
# @then('they should see the dashboard')
# def step_impl(context):
#     print("User sees the dashboard")

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('the user launches the Chrome browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()  # Or specify path if chromedriver is not in PATH
    context.driver.maximize_window()

@when('the user opens the OrangeHRM login page')
def step_open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)

@when('clicks on the login button')
def step_click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('the user should see the OrangeHRM dashboard')
def step_verify_dashboard(context):
    time.sleep(3)  # Wait for dashboard to load
    assert "dashboard" in context.driver.current_url.lower(), "Dashboard not found"

@then('close the browser')
def step_close_browser(context):
    context.driver.quit()

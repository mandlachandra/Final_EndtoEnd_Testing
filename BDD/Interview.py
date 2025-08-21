# #"What is Python BDD framework and how did you use it?”
# # we used python BDD with selenium for UI Automation
# # project
# # ->features
# # --->login.feature
# #
# # ->steps
# # ---->test_login_steps
# #
# # ->pages
# # ----->login_pages(page object model)
# #
# # ->conftest.py(setup/teardown)
# # ->requirments.txt
#
# # 1.Feature file
# # Feature : Login functionality
# #     Scenario : Valid login
# #         Given I launch the browser
# #         When I open OrangeHRM login page
# #         And I enter username "Admin" and password "admin123"
# #         And I click on login button
# #         Then I should see the dashboard page
#
# # 2.Step Definitions(test_login_steps.py)
# from pytest_bdd import scenarios ,given,when,then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# #link to feature file
#     scenarios('../features/login.feature')
#
#     @given('I launch the browser')
#     def launch_browser():
#         global driver
#         driver = webdriver.Chrome()
#         driver.mazimize_window()
#
#     @when('I open OrangeHRM login page')
#     def open_login_page():
#         driver.get("https://orangehrm.com")
#
#     @when('I enter username "Admin" and password "admin123"')
#     def enter_credentials():
#         driver.find_element(By.ID,'username').send_keys('admin')
#         driver.find_element(By.ID,'password').send_keys('admin123')
#
#     @when('I click on login button')
#     def click_login():
#         driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
#     @then('I should see the dashboard')
#     def verify_dashboard():
#         assert "dashboard" in driver.current_url.lower()
#         driver.quit()
#
#
# #what is background in feature file
# #In Gherkin feature file , background is used to define steps that are common to all scenarios in a feature
# #this steps will run before each scenario in the feature file
#
# #syntax
# # Background:
# #     Given I launch the browser
# #     And I open the orangeHrm login page
#
# # Feature: Login functionality for OrangeHRM
# #
# #   Background:
# #     Given I launch the browser
# #     And I open the OrangeHRM login page
# #
# #   Scenario: Successful login with valid credentials
# #     When I enter username "Admin" and password "admin123"
# #     And I click on login button
# #     Then I should see the dashboard page
# #
# #   Scenario: Login fails with invalid credentials
# #     When I enter username "Admin" and password "wrongpass"
# #     And I click on login button
# #     Then I should see an error message "Invalid credentials"

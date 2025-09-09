# 1.Test Discovery
# Pytest automatically discovers test files and test methods
# Rules:
# Test file name should start with test_ or end with _test.py
# Test function/method names should start with test_
#
# def test_valid_login():
#     assert True
import pytest

import pytest_selenium_python.All_Concepts

# 2.Assertions
# Pytest uses simple assert statements
#
# def test_title(driver):
#     driver.get("https://www.google.com")
#     assert driver.title == "Expected title", "Title mismatch"

# 3.Fixture(@pytest.fixture)
# # Fixtures help set up preconditions and teardown steps
# # ex.conftest.py
# # import pytest
# # from selenium import webdriver
# #
# # @pytest.fixture(scope="class")
# # def initialize_driver(request):
# #     driver = webdriver.Chrome()
# #     driver.maximize_window()
# #     request.cls.driver = driver
# #     yield
# #     driver.quit()
# #
# # Example usage in test
# # import pytest
# #
# # @pytest.mark.usefixtures("initialize_driver")
# # class TestExample:
# #     def test_google(self):
# #         self.driver.get("https://google.com")

# 4.conftest.py
# This is a special file where common fixtures are stored
# It is auto-loaded by pytest no need to import manually
# Use it for:
#     Fixtures
#     Hooks
#     Configs

# 5.Base Test Class
# A BaseTest class can be used to apply common fixtures and logging
# from utils.logger import get_logger
#
# @pytest.mark.usefixtures("initialize_driver")
# class BaseTest:
#
#     log = get_logger

# 6.pytest markers(@pytest.mark)
# used to label or group tests
#
# common markers:
# @pytest.mark.smoke
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.usefixtures
# @pytest.mark.parametrize

@pytest.mark.smoke
def test_login():
    pass

# 7.Parameterize(@pytest.mark.parametrize)
# Allows data-driven testing - run the same test with multiple inputs
#
# @pytest.mark.parametrize("username,password" [
#                 ("user1","pass1"),
#                 ("admin1","pass2")
# ])
# def test_login(username,password):
#     print(f"Logging in with {username}/{password}")

# 8.Command line options
# pytest supports various CLI options to run tests with more control
#
# pytest -v -s --html=report.html --capture=tee-sys
# -v = verbose
# -s = show print statements
# --html = generate HTML Report
# --capture=tee-sys = show logs in both console and file

# 9.Grouping and Running specific tests
# Run tests based on:
# Module name
# Class name
# Marker name
# Line number

# #if you want to execute specific test
# pytest tests/testlogin.py::TestLogin::test_valid_login


#
# pytest -m "smoke"
# To run tests that are marked with specific label
#
# pytest -k "valid"
# To run any test where the name contains "valid"
#
# pytest
# To run all tests
#
# 10.Pytest HTML reports
# pytest --html = report/report.html --self-contained-html


# 11.Allure reports integration
# Use --alluredir=report to generate results, then
# allure serve reports/


# Hooks(Optional advanced feature)
# Customize pytest behaviour using hooks like pytest_runtest_setup
#
# def pytest_runtest_setup(item):
#     print(f"setting up {item.name}")

# 13.Logging(With logger or print)
# Use a custom logger to record test steps and failures
# import logging
# def get_logger():
#     logger =logging.getlogger("TestLogger")
#     ....
# Use in tests
# self.log.info("Login successful")

# 14.pytest.ini Configuration
# Configure default test settings
# [pytest]
# addopts = -v -s -ra --html=report/report.html --self-contained-html
# markers =
#     smoke : smoke tests
#     regression : regression tests

# 15.Skip and Xfail
# @pytest.mark.skip : skip test
# @pytest.mark.xfail : expected to fail
#
# @pytest.mark.skip(reason="not ready")
# def test_skip_me():
#     pass

# 16.Custom command line arguments
# Add you own flags using pytest_addoption
#
# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store",default = "chrome")
#
# Then access in fixture
#
# @pytest.fixture(scope="class")
# def initialize_driver(request):
#     browser = request.config.getoption("--browser")

# 17.Fixture with Scope
# function = runs for every test function
# class = runs once per class
# module = once per file
# session = once per test session

# 18.Test failure with screenshots
#
# In Conftest.py capture screenshot on failure
#
# @pytest.hookimpl(tryfirst=True,hookWrapper=True)
# def pytest_runtest_makereport(item,call):
#     outcome = yield
#     result = outcome.get_result()
#     if result.when == "call" and result.failed:
#         driver=item.cls.driver
#         driver.save_screenshot(f"screenshot/{item.name}.png")


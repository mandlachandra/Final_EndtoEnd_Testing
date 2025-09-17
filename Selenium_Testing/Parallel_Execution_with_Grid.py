# Step 1: Start Selenium Grid
#
# You need to set up a Selenium Grid Hub and Nodes.
#
# 1. Start Hub
# java -jar selenium-server-standalone-<version>.jar hub
#
#
# Hub will be available at:
# 👉 http://localhost:4444/grid/console
#
# 2. Start Node
# java -jar selenium-server-standalone-<version>.jar node --hub http://localhost:4444
#
#
# Now your Hub is managing requests, and Nodes will run browsers (Chrome, Firefox, etc.).
#
# 🔹 Step 2: Install pytest-xdist
#
# This plugin helps in parallel execution.
#
# pip install pytest-xdist
#
# 🔹 Step 3: conftest.py (Driver Setup for Grid)
#
# Here we’ll configure driver initialization pointing to Selenium Grid Hub.
#
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope="class")
# def init_driver(request, browser):
#     if browser == "chrome":
#         capabilities = {"browserName": "chrome"}
#     elif browser == "firefox":
#         capabilities = {"browserName": "firefox"}
#     else:
#         raise Exception("Browser not supported!")
#
#     # Selenium Grid Hub URL
#     grid_url = "http://localhost:4444/wd/hub"
#     driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
#     driver.maximize_window()
#
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#
#
# @pytest.fixture(scope="class")
# def browser(request):
#     return request.config.getoption("--browser")
#
# 🔹 Step 4: Example Test Cases
#
# test_sample1.py
#
# import pytest
#
# @pytest.mark.usefixtures("init_driver")
# class TestGoogle:
#
#     def test_title(self):
#         self.driver.get("https://www.google.com")
#         assert "Google" in self.driver.title
#
#     def test_search(self):
#         self.driver.get("https://www.google.com")
#         search_box = self.driver.find_element("name", "q")
#         search_box.send_keys("Selenium Grid with Pytest")
#         search_box.submit()
#         assert "Selenium" in self.driver.page_source
#
#
# test_sample2.py
#
# import pytest
#
# @pytest.mark.usefixtures("init_driver")
# class TestPython:
#
#     def test_title(self):
#         self.driver.get("https://www.python.org")
#         assert "Python" in self.driver.title
#
#     def test_downloads(self):
#         self.driver.get("https://www.python.org/downloads/")
#         assert "Download" in self.driver.page_source
#
# 🔹 Step 5: Run Tests in Parallel
#
# Example: Run 4 tests in parallel
#
# pytest -n 4 --browser=chrome
#
#
# If you want to run tests on multiple browsers (Chrome + Firefox):
#
# pytest -n 4 --browser=chrome
# pytest -n 4 --browser=firefox
#
#
# ✅ This way:
#
# Selenium Grid manages distributed execution across nodes.
#
# pytest-xdist runs test cases in parallel.
#
# You can scale across multiple machines and browsers.
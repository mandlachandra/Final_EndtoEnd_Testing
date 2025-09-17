# What is Cross-Browser Testing?
#
# Cross-browser testing means running the same test cases on different browsers (Chrome, Firefox, Edge, Safari, etc.) to ensure the application works consistently.
#
# 🔹 Step 1: Add Browser Options in conftest.py
#
# We’ll make the driver configurable to run different browsers.
#
# import pytest
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="Type in browser: chrome or firefox"
#     )
#
# @pytest.fixture(scope="class")
# def init_driver(request):
#     browser = request.config.getoption("--browser")
#
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome()
#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox()
#     elif browser.lower() == "edge":
#         driver = webdriver.Edge()
#     else:
#         raise ValueError(f"Browser '{browser}' is not supported")
#
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
# 🔹 Step 2: Write Test Cases
#
# test_cross_browser.py
#
# import pytest
#
# @pytest.mark.usefixtures("init_driver")
# class TestCrossBrowser:
#
#     def test_google_title(self):
#         self.driver.get("https://www.google.com")
#         assert "Google" in self.driver.title
#
#     def test_python_title(self):
#         self.driver.get("https://www.python.org")
#         assert "Python" in self.driver.title
#
# 🔹 Step 3: Run Tests on Different Browsers
#
# 👉 Run on Chrome:
#
# pytest test_cross_browser.py --browser=chrome -v
#
#
# 👉 Run on Firefox:
#
# pytest test_cross_browser.py --browser=firefox -v
#
#
# 👉 Run on Edge:
#
# pytest test_cross_browser.py --browser=edge -v
#
# 🔹 Step 4: Parallel Cross-Browser (Using pytest-xdist)
#
# If you want Chrome + Firefox in parallel:
#
# pytest -n 2 --browser=chrome --browser=firefox
#
#
# ⚠️ But Pytest --browser takes only one value by default. To support multi-browser in the same run, we can parametrize the fixture.
#
# 🔹 Step 5: Parametrize for Multiple Browsers
#
# Update conftest.py:
#
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def init_driver(request):
#     browser = request.param
#
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError("Browser not supported!")
#
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
#
# Now when you run:
#
# pytest -v
#
#
# 👉 Each test will automatically run on both Chrome and Firefox.
#
# ✅ So, you have two options:
#
# Single browser run (via --browser)
#
# Cross-browser parametrize run (via params=[...] in fixture)
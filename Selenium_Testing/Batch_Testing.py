#Q1: What is Batch Testing in Manual Testing?
# Batch Testing is a process of executing a group of test cases together (as a suite or batch) instead of
# running individually. It is usually done when test cases are logically grouped , belong to s specific module
# or need regression coverage
#
# EX: Running all "Login module" test cases as a batch

# Q2: Why do we perform batch testing?
# ->To save time by executing multiple test cases together
# ->To ensure complete test coverage for a feature or modulefinder
# ->To validate end-to-end scenarios where multiple test cases are interdependent.

# Q3: How do you prepare test cases for batch testing manually?
# ->Group test cases based on module/priority
# ->Arrange them in a sequence (if dependent)
# ->Create a test suite document or check list
# ->Execute test cases step by step and mark Pass/Fail

# Q4: What challenges do you face in manual batch testing?
# ->Human errors while executing large batches
# ->Time-consuming compared to automation
# ->Regression tests become repetitive

# Q5: How do you perform batch testing in Selenium Python using Pytest?
# ->In pytest batch tetsing is done by:
#     placing multiple test files inside  a tests/folder
#     Running them together using:
#     pytest tests/
# Pytest automatically discovers and execute all test cases in a batch
#
# Q6: How do you run selected test cases in a batch (not all)?
# user markers:
# import pytest
# @Pytest.nark.smoke
# def test_login():
#     assert True
#
# @pytest.nark.regression
# def test_cart():
#     assert True

#Run only smoke test
#pytest -m "smoke"

# Q7: How do you run batch tests in parallel in Pytest?
# install plugin: pip install pytest-xdist
# run tests in parallel
# pytest -n 4
# ->This runs batch tests on 4 parallel threads to save time

# Q8: How do you integrate batch testing with Jenkins?
# ->push selenium+pytest projects to GitHub
# ->In Jenkins create a job and configure git repo
# ->Add build command
# pytest tests/ --alluredir=allure-results
# Post build publish Allure Reports to see batch execution results

# Q9: How do you handle dependencies between test cases in batch execution?
# ->Best practice : Keep test cases independent
# ->if independent: use pytest-ordering plugin

# import pytest
#
# @pytest.mark.order(1)
# def test_login():
#     assert True
#
# @pytest.mark.order(2)
# def test_plp():
#     assert True
#
# Q10: What reports do you use to analyze batch testing results in automation?
# ->Allure reports ->Detailed HTML with Passes/Failed/Skipped
# ->pytest HTML Report
# pytest --html = report.html
# Jenkins JUnit plugin for CI/CD
#
# Q11: What are challenges in batch testing with Selenium + Pytest?
# ->Flaky tests due to synchronization issues ->solved by explicit waits
# ->Dynamic elements ->Solved by robust locators(XPATH,CSS)
#->Parallel execution failures ->solved by thread-safe Webdriver instances
#
# Q12: Example – Running batch tests with Allure Reports
# pytest tests/ --alluredir=allure-results
# allure serve allure-results
# ->Opens a report showing how many test cases in batch passed/failed

# 3. Batch Execution using Test Suite (Unittest)
# import unittest
#
# class TestLogin(unittest.TestCase):
#     def test_valid_login(self):
#         self.assertEqual(1, 1)
#
#     def test_invalid_login(self):
#         self.assertEqual(1, 1)
#
# class TestCheckout(unittest.TestCase):
#     def test_add_to_cart(self):
#         self.assertTrue(True)
#
# # Batch Suite
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestLogin))
#     suite.addTest(unittest.makeSuite(TestCheckout))
#     return suite
#
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

# 4. Batch File Execution (Windows .bat File)
# To run Selenium automation in batch, teams create a .bat file
# ex:
# run_tests.bat
#
# echo Running Michaels Automation Batch Tests....
# pytest tests/ --html=report.html --self.contained-html
# pause
# ->Double clicking this file executes the whole batch suite and generates a report

# 5. Batch Testing in CI/CD (Jenkins)
# ->In real-time (Michaels project), we had jenkins configured.
# Pipelines triggered batch test execution after every deployment
# ->Different batches (smoke,regression,API) were scheduled
# ->smoke batch after every build.
# ->regression batch nightly
# ->Reports shared via Allure/Extent/HTML report



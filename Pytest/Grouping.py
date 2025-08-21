import pytest

class TestClass:

    @pytest.mark.sanity
    def test_methodA(self):
        print("This is login by email")
        assert 1 ==1

    @pytest.mark.sanity
    def test_methodB(self):
        print("This is login by facebook")
        assert 1==1

    @pytest.mark.regression
    def test_methodC(self):
        print("this is login by wtsup")
        assert 1==1


    def test_methodD(self):
        print("this is login by yahoo")
        assert 1==1

#pytest -v -s -m "sanity" pytest\grouping
#pytest -v -s -m "regression" pytest\grouping
#pytest -v -s -m "sanity and regression" pytest\grouping

#Run all test cases (Batch Execution)
# pytest tests/

#Run single test file
# pytest tests/test_login.py

#run single function from a test case
# pytest tests/test_login.py::test_valid_login

#Group test cases with markers
# pytest -v -s -m "smoke" pytest\grouping

#Run multiple files together
# pytest tests/test_login.py tests/test_cart.py

# pytest -n 4

# Generate Reports after Execution
# pytest --html = report.html
#
# pytest --allure.dir = allure-results
# allure serve allure-results

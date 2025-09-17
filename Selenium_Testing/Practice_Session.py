# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# try:
#     driver.get("www.google.com")
#     driver.maximize_window()
#     time.sleep(2)
#
# finally:
#     driver.quit()

import pytest

# @pytest.mark.parametrize("a,b,result",[(2,3,5),(5,5,10),(10,5,15)])
# def test_add(a,b,result):
#     assert a+b == result
#
@pytest.mark.parametrize("a,b,result",[(2,3,5),(5,5,10),(10,5,15)])
def test_add(a,b,result):
    assert a + b ==result

@pytest.mark.smoke
def test_login():
    assert True

#Running with markers
# pytest -m "smoke"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
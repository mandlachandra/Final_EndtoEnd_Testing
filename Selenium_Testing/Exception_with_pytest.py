import pytest
from selenium.common.exceptions import NoSuchElementException

def test_invalid_locator(driver):
    with pytest.raises(NoSuchElementException):
        driver.find_element("id","non_existent_element")


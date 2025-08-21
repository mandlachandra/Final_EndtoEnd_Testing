import pytest
import allure

class TestSample:

    def test_addition(self):
        a, b = 5, 3
        assert a + b == 8

    def test_subtraction(self):
        a, b = 10, 4
        assert a - b == 6

    def test_multiplication(self):
        a, b = 7, 6
        assert a * b == 42

    def test_division(self):
        a, b = 20, 5
        assert a / b == 4

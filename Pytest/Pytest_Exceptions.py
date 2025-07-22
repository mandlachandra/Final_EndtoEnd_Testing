import pytest

#Simple execution test
def divide(a,b):
    return a/b

# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(10,0)
#
# #Check message exceptions
# def test_zero_division_message():
#     with pytest.raises(ZeroDivisionError,match="division by zero"):
#         divide(5,0)

#capture the exception object
def test_capture_exception():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(1,0)
    assert str(excinfo.value) == "division by zero"

#check for multiple exceptions
def test_multiple_exceptions():
    with pytest.raises((ZeroDivisionError,TypeError)):
        divide("10",2)


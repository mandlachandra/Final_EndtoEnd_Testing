import pytest

class TestClass:

    def test_methodA(self):
        print("This is methoda")
        assert 1==1

    def test_methodB(self):
        print("this is methodb")
        assert 1==1
    @pytest.mark.skip
    def test_methodC(self):
        print("this is methodc")
        assert 1==1
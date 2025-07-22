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

    @pytest.mark.regression
    def test_methodD(self):
        print("this is login by yahoo")
        assert 1==1

#pytest -v -s -m "sanity" pytest\grouping
#pytest -v -s -m "regression" pytest\grouping
#pytest -v -s -m "sanity and regression" pytest\grouping

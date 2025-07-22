#By default pytest runs tests sequentially
#To run tests in parallel we need to use the plugin
#pip install pytest-xdist

#basic command to run tests
#pytest -n <num_workers>
#Here <num_workers> = number of CPUS/threads you want to use
#Example run 4 tests at the same time
#pytest -n 4
#This splits the test files across 4 workers
#tests
    #-test_login.py
    #-test_signup.py
    #-test_profile.py
    #-test_logout.py

#run all tests in parallel
#pytest -n 4 teste/
#Each worker picks a test file and runs them simultaneously

import time

def test_login_valid():
    time.sleep(2)
    print("login valid test")
    assert True

def test_login_invalid():
    time.sleep(2)
    print("login invalid test")
    assert True

def test_signup_valid():
    time.sleep(2)
    print("signup valid")
    assert True

def test_signup_invalid():
    time.sleep(2)
    print("signup invalid")
    assert True
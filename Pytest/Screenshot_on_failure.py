#Understanding the decorator
# @pytest.hookimpl(tryfirst=True,hookwrapper=True)
# #pytest.hookimpl = This tells pytest that this is a hook function
# #tryfirst=True ->Runs this hook before any other implementation of the same hook
# #hookwrapper=True ->Allows you to wrap around the actual pytest hook execution
# #you call yield to let pytest run the rest of the hook and you can do work before and after it.
#
# #The Hook function
# def pytest_runtest_makereport(item,call):
#
# #This hook is called after each phase of a test (setup,call,teardown)
# #parameters:
# #item ->The test function or method object being run
# #call ->Contains the result of the phase(setup,call or teardown)
#
# #Yield and getting the result
# outcome = yield
# result = outcome.get_result()

#yield ->Lets pytest run the actual test before continuing.
# outcome.get_result ->Retrieves the result object for the test phase
#
# #Checking the failures
# if result.when =="call" and result.failed:
#
# result.when ->indicates the phase
# "setup" ->before the execution
# "call" ->the actual test body
# "teardown" ->after the test execution
#
# "call" ->means we are checking the main execution of the test
# result.failed ->means the test failed in that phase
#
# #capturing screenshot
# driver = item.cls.driver
# driver.save_screenshot(f"screenshot/{item.name}.png")
#
# #item.cls.driver ->Accesses the driver instance from the test class (item.cls is the test class).
# driver.save_screenshot(path) ->saves the screenshot to the given path
# f"screenshot/{item.name}.png" ->File nameis the test name(e.g, test_valid_login.png)








import pytest

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver'] #get driver fixture
        driver.save_screenshot(f"screenshots/{item.name}.png")
        print(f"\n screenshot failed for failed test:{item.name}")

# #In pytest a hook is a way to customize and extend pytest behaviour
# # Hooks are predefined functions in pytest like pytest_runtest_setup,pytest_sessionstart etc
# #
# # Hooks are defined in a conftest.py file
#
# #Common pytest hooks
# import pytest
#
# # 1.pytest_sessionstart
# # Called before any tests are run(session level setup)
# #
# # def pytest_sessionstart(session):
# #     print("\n===>pytest session is starting")
#
#
# # 2.pytest_sessionfinish
# # called after tests are finish(session level teardown)
# #
# # def pytest_sessionfinish(sessison,exitfinish):
# #     print("\n===>pytest session finished with exit status",exitstatus)
#
# # 3.pytest_runtest_setup
# # called before each test is executed
# #
# # def pytest_runtest_setup(item):
# #     print("\n====>setting up for test:",item.name)
#
# # 4.pytest_runtest_teardown
# # called after each test
# # def pytest_runtest_teardown(item,nextitem):
# #     print("\n===>Tearing down after test:",item.name)
#
# # 5.pytest_runtest_call
# # called when the actual test function runs
# # def pytest_runtest_call(item):
# #     print("Running test:",item.name)
#
# # 6.pytest_collection_modifyitems
# # modify the collected test cases(filter,reprder,tag)
# # def pytest_collection_modifyitems(session,config,items):
# #     for item in items:
# #         if "login" in item.name:
# #             item.add_marker(pytest.mark.smoke)
#
# # 7.pytest_configure
# # called after command line options and conftest files are passed
# #
# # def pytest_configure(config):
# #     print("\n--->pytest configuration loaded")
#
# # 8.pytest_unconfigure
# # called at the very end , before pytest exits
# #
# # def pytest_unconfigure(config):
# #     print("\n====>pytest cleanup before exit")
#
# # 9.pytest_addoption
# # Add custom command line option to pytest
# # def pytest_addoption(parser):
# #     parser.addoption("--browser",action="store",default = "chrome")
# #
# # Then access it in tests
# #
# # @pytest.fixture
# # def browser(request):
# #     return request.config.getoption("--browser")
# #
# # RUN:
# # pytest --browser=firefox
#
# def pytest_runtest_makereport(item, call):
#     if call.when =="call" and call.excinfo is not None:
#         print("Test failed, take screenshot!")

import pytest

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver'] #get driver fixture
        driver.save_screenshot(f"screenshots/{item.name}.png")
        print(f"\n screenshot failed for failed test:{item.name}")

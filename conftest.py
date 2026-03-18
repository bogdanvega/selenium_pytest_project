import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    chrome_options = webdriver.ChromeOptions()

    # Avoid Google Password Manager pop-up
    chrome_options.add_argument("--guest")

    # Zoom out to ensure all UI elements are visible during automation
    chrome_options.add_argument("--force-device-scale-factor=0.8")  # 80% zoom

    # Start browser maximized
    chrome_options.add_argument("--start-maximized")

    # Start driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()

    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    report = outcome.get_result()

    # only take screenshot when test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            file_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(file_name)

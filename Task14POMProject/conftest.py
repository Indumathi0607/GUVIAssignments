import os.path

import pytest
from pytest_html import extras
from selenium import webdriver

from Pages.zen_login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://v2.zenclass.in/login")
    driver.maximize_window()

    lp = LoginPage(driver)
    assert lp.get_login_header() == 'Login', f"Expected title: Login, but actual {lp.get_login_header}"

    yield driver
    driver.quit()


# Adding HTML report title
def pytest_html_report_title(report):
    report.title = ("Test automation report for task 14 with Page Object Model")

#create screenshot folder to add screenshots
screenshot_dir = "Screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs("Screenshots")

#Method to take screenshot and add it to html report
@pytest.hookimpl(tryfirst= True, hookwrapper= True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report= outcome.get_result()

    if report.when == "call":
        #get the driver from the fixture
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Save screenshot to file
                screenshot_path = os.path.join(screenshot_dir, f"screenshot_{item.name}.png")
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to {screenshot_path}")


                #Capture screenshot as Base 64 to embed it in html report
                screenshot = driver.get_screenshot_as_base64()

                #add screenshot to HTML report
                report.extras.append(extras.image(screenshot, name = f"screenshot_{item.name}"))

            except Exception as e:
                report.extras.append(extras.text(f"Failed to capture the screenshot: {str(e)}"))

        else:
            print(f"No driver found for test {item.name}")
            report.extras.append(extras.text("No driver available for screenshot"))



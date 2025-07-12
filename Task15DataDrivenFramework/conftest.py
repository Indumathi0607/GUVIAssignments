import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    #Wait for the login page to load
    lp = LoginPage(driver)
    assert lp.is_org_title_displayed() == True, f"Login page is not loaded"

    yield driver
    driver.quit()

# Adding HTML report title
def pytest_html_report_title(report):
    report.title = ("Test automation report for Data Driven Framework")

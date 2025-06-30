import pytest
from selenium import webdriver
from PageActions.login_actions import LoginActions


@pytest.fixture
def driver():

    #Setting up headless browser execution
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.guvi.in/") #Launch GUVI website

    #navigate to Login screen
    login_action = LoginActions()
    login_action.get_into_login_webpage(driver)

    yield driver #returns driver
    driver.close()

#Adding HTML report title
def pytest_html_report_title(report):
    report.title ="Test automation report for login validations"


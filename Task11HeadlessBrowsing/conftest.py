import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    #Setting up headless browser execution
    options = Options()

    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.guvi.in/") #Launch GUVI website
    driver.maximize_window()

    yield driver #returns driver
    driver.close()

#Adding HTML report title
def pytest_html_report_title(report):
    report.title ="Test automation report for login validations"


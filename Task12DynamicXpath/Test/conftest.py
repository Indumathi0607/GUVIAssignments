import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    # Launching the chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    #Get into Guvi webpage
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

#Method to add test report title
def pytest_html_report_title(report):
    report.title = "Test automation report for validating xpath of menu list in GUVI homepage"


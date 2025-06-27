import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    # Launching the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    #Open the jqueryui website
    driver.get("https://jqueryui.com/droppable/")

    #Switch to iFrame
    iframe = driver.find_element(By.XPATH, "//iframe[@class = 'demo-frame']")
    driver.switch_to.frame(iframe)

    yield driver
    #teardown code
    driver.quit()

#Method to add test report title
def pytest_html_report_title(report):
    report.title = "Test automation report for validating drag and drop"

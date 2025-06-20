import pytest
from pytest_html import extras
from selenium import webdriver

#setting up global dictionary to store web page info like title, url
webpage_info = {}

#Adding fixture to launch the browser and quit it after the execution
@pytest.fixture
def setup():
    # Launching the edge browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # Get into the sauce demo webpage
    driver.get("https://www.saucedemo.com/")
    webpage_info['title'] = driver.title
    webpage_info['url_before_login'] = driver.current_url

    yield driver # Returns the driver to test methods
    driver.quit() # closes the browser after executing the tests.

#Setup the title for the html test report
def pytest_html_report_title(report):
    report.title = "SauceDemo Test Automation Report"

#Method to include the web page info under title of the HTML report as prefix
def pytest_html_results_summary(prefix, summary, postfix):
    title= webpage_info.get('title', 'N/A') #N/A returns N/A in html report if the value is empty
    url_before_login = webpage_info.get('url_before_login', 'N/A')
    url_after_login = webpage_info.get('url_after_login', 'N/A')

    prefix.extend([
        f"<p><strong>Title of web application: {title}</strong></p>",
        f"<p><strong>URL of web application before login: {url_before_login}</strong></p>",
        f"<p><strong>URL of web application after login: {url_after_login}</strong></p>",
    ])







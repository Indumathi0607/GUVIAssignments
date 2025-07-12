import pytest
from selenium import webdriver

from pages.home_page import HomePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    #Launch web browser
    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
    driver.maximize_window()

    hp = HomePage(driver)
    hp.is_home_page_title_displayed()

    yield driver
    driver.quit()


#Define html report title
def pytest_html_report_title(report):
    report.title = ("Task16 get world count test report")
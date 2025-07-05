from operator import truediv

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_title = (By.XPATH, "//p[text()='Dashboard']")
        self.user_profile = (By.CLASS_NAME, "profile-click-icon-div")
        self.logout = (By.XPATH, "//div[@class='user-profile-notify-container']//div[text()='Log out']")
        self.alert = (By.XPATH, "//button[@class='custom-close-button']")

    def get_dashboard_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_title)
        ).text.strip()

    def click_user_profile(self):
        self.driver.find_element(*self.user_profile).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logout)
        ).click()

    def perform_logout(self):
        self.driver.find_element(*self.dashboard_title).click()
        self.click_user_profile()
        self.click_logout()

    def handle_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.alert)).click()
        except NoAlertPresentException:
            return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.organization_name = (By.CLASS_NAME, "orangehrm-login-branding")
        self.username_textbox = (By.XPATH, "//input[@name = 'username']")
        self.password_textbox = (By.XPATH, "//input[@name = 'password']")
        self.login_button = (By.XPATH, "//button[@type= 'submit']")
        self.login_error_message = (By.XPATH, "//p[@class = 'oxd-text oxd-text--p oxd-alert-content-text']")

    def is_org_title_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.organization_name)
        ).is_displayed()

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_login_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_error_message)
        ).text

    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

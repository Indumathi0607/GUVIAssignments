from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    # using POM to get login page locators
    def __init__(self, driver):
        self.driver = driver
        self.login_header = "login-heading"
        self.username_label = "//label[text() = 'Email Address']"
        self.username_textbox = "//input[@type='email']"
        self.password_label = "//label[text() = 'Password']"
        self.password_textbox = "//input[@type='password']"
        self.login_button = "//a[@id = 'login-btn']"
        self.username_error = "//div[@class= 'invalid-feedback is-invalid']"
        self.password_error = "//div[@id='passwordGroup']/div[@class = 'invalid-feedback']"

    # Method to close Chrome login auto suggestion.
    def close_chrome_login_suggestion(self):
        self.driver.find_element(By.CLASS_NAME, self.login_header).click()

    # Method to find username label
    def get_username_label(self):
        try:
            return self.driver.find_element(By.XPATH, self.username_label).text.strip()
        except NoSuchElementException:
            return None

    # Method to focus on username textbox
    def get_username_textbox(self):
        return self.driver.find_element(By.XPATH, self.username_textbox)

    # Method to fill username
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)

    # Method to find password label
    def get_password_label(self):
        try:
            return self.driver.find_element(By.XPATH, self.password_label).text.strip()
        except NoSuchElementException:
            return None

    # Method to password text box
    def get_password_textbox(self):
        return self.driver.find_element(By.XPATH, self.password_textbox)

    # Method to fill password
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    # Method to click login
    def submit_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_button))
        ).click()

    # Method to get invalid username error
    def get_username_error(self):
        return self.driver.find_element(By.XPATH, self.username_error).text.strip()

    # Method to get invalid password error
    def get_password_error(self):
        return self.driver.find_element(By.XPATH, self.password_error).text.strip()

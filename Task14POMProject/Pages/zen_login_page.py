from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_header = (By.XPATH, "//div[text() = 'Login']")
        self.email_title = (By.XPATH, "//label[text() = 'Email']")
        self.email_textbox = (By.XPATH, "//input[@placeholder= 'Enter your mail']")
        self.email_image_container = (By.CLASS_NAME, "email-icon-container")
        self.password_title = (By.XPATH, "//label[text() = 'Password']")
        self.password_textbox = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.password_visibility_icon = (By.XPATH, "//button[@aria-label='toggle password visibility']")
        self.signin_button = (By.XPATH, "//button[@type='submit']")
        self.login_error_message = (By.XPATH, "//div[@class='password-input']//p")

    #Get the 'Login' text to validate the login page loaded
    def get_login_header(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_header)
        ).text

    #Return the text of Username field 'Email'
    def get_email_title(self):
        return self.driver.find_element(*self.email_title).text

    #Return the placeholder text of email
    def get_email_placeholder_text(self):
        return self.driver.find_element(*self.email_textbox).get_attribute('placeholder')

    #Verify presence of email container
    def is_email_container_image_displayed(self):
        return self.driver.find_element(*self.email_image_container).is_displayed()

    #Enter email address
    def enter_email_id(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    #Return the title text of Password field 'Password'
    def get_password_title(self):
        return self.driver.find_element(*self.password_title).text

    #Return the placeholder text of password
    def get_password_placeholder_text(self):
        return self.driver.find_element(*self.password_textbox).get_attribute('placeholder')

    #Verify presence of password visibility icon
    def is_password_visibility_icon_displayed(self):
        return self.driver.find_element(*self.password_visibility_icon).is_displayed()

    #Enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    #Click on Sign in button
    def click_sign_in_button(self):
        self.driver.find_element(*self.signin_button).click()

    #Get the error text for login with empty credentials
    def get_login_error_message(self):
        error_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_error_message)
        ).text

        return error_text

    #perform login
    def perform_login(self, username, password):
        self.enter_email_id(username)
        self.enter_password(password)
        self.click_sign_in_button()

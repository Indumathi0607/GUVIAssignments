from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageActions.login_actions import LoginActions
from pages.login_page import LoginPage


class TestGUVILogin:

    # 1. Validate login screen URL
    def test_login_url(self, driver):

        #Creating login page object
        login_action = LoginActions()
        login_action.get_into_login_webpage(driver)

        login_url = driver.current_url
        assert login_url == "https://www.guvi.in/sign-in/", f"expected URL: https://www.guvi.in/sign-in/ and the actual is {login_url}"

    # 2. Validate username input box is visible and enabled
    def test_username_textbox(self, driver):

        # using POM to get login page locators
        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()

        login_action = LoginActions()
        login_action.validate_input_textbox(login_page.get_username_label(), login_page.get_username_textbox(), "Email Address")

    # 3. Validate password input box is visible and enabled
    def test_password_textbox(self, driver):

        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()

        login_action = LoginActions()
        login_action.validate_input_textbox(login_page.get_password_label(), login_page.get_password_textbox(), "Password")

    # 4.1 Validate submit button works fine- negative testcase
    def test_login_fails_with_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()

        try:
            login_page.submit_login()
            driver.save_screenshot("screenshots/Login_empty_credentials.png")

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, login_page.password_error))
            )

            error_message = login_page.get_password_error()

            assert error_message.strip() == "Hey, Did you forgot your password? Try again.", f"Expected error message 'Hey, Did you forgot your password? Try again.' But got {error_message}"

        except (ElementNotInteractableException, NoSuchElementException) as e:
            print(f"Caught {type(e).__name__} for Login button. The error is {e}")
            assert False, f"Caught error {e} with Login button"

    # 4.2 Validate Submit button woks fine - negative testcase
    def test_login_fails_with_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()
        login_page.enter_username("abcdef_123@qwe.in")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, login_page.username_error))
        )

        driver.save_screenshot("screenshots/Login_invalid_username.png")
        actual_error = login_page.get_username_error().strip()
        assert actual_error == "Oh! No profile exists with this Email ID. Click here to Sign Up", f"Expected message: 'Oh! No profile exists with this Email ID. Click here to Sign Up' and actual is {actual_error}"

    # 4.3 Validate Submit button woks fine - negative testcase
    def test_login_fails_with_invalid_password(self, driver):

        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()

        # Fill in username, password and submit login
        login_page.enter_username("Removed") #removed valid user name after execution
        login_page.enter_password("123456")
        login_page.submit_login()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, login_page.password_error))
        )

        # validate the error message
        actual_error = login_page.get_password_error().strip()
        assert actual_error == "Incorrect Email or Password", f"Expected message: 'Incorrect Email or Password' and actual is {actual_error}"

    # 4.4 Validate submit button works fine - positive testcase
    def test_login_success_with_valid_password(self, driver):

        #Creating object for login page
        login_page = LoginPage(driver)
        login_page.close_chrome_login_suggestion()

        # Fill in username, password and submit login
        login_page.enter_username("Removed")#removed valid user name after execution
        login_page.enter_password("Removed")#removed valid password after execution
        login_page.submit_login()
        driver.save_screenshot("/screenshots/T7_1.png")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Paid Courses']"))
        )

        driver.save_screenshot("screenshots/Login_success.png")

        # validate the error message
        current_url = driver.current_url
        assert current_url == "https://www.guvi.in/courses/?current_tab=myCourses", f"Expected 'https://www.guvi.in/courses/?current_tab=myCourses', but actual: {current_url}"

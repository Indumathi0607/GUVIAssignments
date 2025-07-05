import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException

from Pages.zen_home_page import Homepage
from Pages.zen_login_page import LoginPage


class TestZenPortalLogin:

    # Test 1: Validate username field
    def test_username_field(self, driver):
        try:
            lp = LoginPage(driver)
            assert lp.get_email_title() == 'Email', f"Expected username field title 'Email', but actual {lp.get_email_title()}"
            assert lp.is_email_container_image_displayed() == True, f"Email container image is not displayed"
            assert lp.get_email_placeholder_text() == 'Enter your mail', f"Missing placeholder text 'Enter your mail'"

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
            print(f"Caught {type(e).__name__}, and the error is {e} ")

    # Test 2: Validate password field
    def test_password_field(self, driver):
        try:
            lp = LoginPage(driver)
            assert lp.get_password_title() == 'Password', f"Missing title 'Password'"
            assert lp.is_password_visibility_icon_displayed() == True, f"Password visibility image is not displayed"
            assert lp.get_password_placeholder_text() == 'Enter your password ', f"Expected 'Enter your password ' but actual is {lp.get_password_placeholder_text()}"

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
            print(f"Caught {type(e).__name__}, and the error is {e} ")

    # Test 3: Login negative scenario
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("", "", "Email and password required!"), ("", "123456", "Email required!"),
                              ("test@gmail.com", "", "Password required!"),
                              ("invalid email", "123456", "*Incorrect mail or password!"),
                              ("abcdedfg@test.in", "1234722", "*Incorrect password!")])
    def test_login_fails_for_invalid_credentials(self, driver, username, password, expected_error_message):
        try:
            lp = LoginPage(driver)
            lp.perform_login(username, password)
            login_error = lp.get_login_error_message().strip()
            driver.save_screenshot("Screenshots/")

            assert login_error == expected_error_message, f"Expected error {expected_error_message}, but actual {login_error}"
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print(f"Caught {type(e).__name__} and error is : {e}")

    # Test 4: Login success and validate submit button
    def test_successful_login(self, driver):
        try:
            lp = LoginPage(driver)
            lp.perform_login("removed_username", "123456")

            hp = Homepage(driver)
            dashboard_title = hp.get_dashboard_title()
            assert dashboard_title == "Dashboard", f"Expected 'Dashboard', but actual {dashboard_title}"
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print(f"Caught {type(e).__name__} and error is : {e}")

    #Test 5: Validate logout
    def test_logout(self, driver):
        try:
            #login with valid credentials
            lp = LoginPage(driver)
            lp.perform_login("removed_username", "123456")

            #Validate dashboard page is loaded?
            hp = Homepage(driver)
            hp.handle_alert()
            dashboard_title = hp.get_dashboard_title()
            assert dashboard_title == "Dashboard", f"Expected 'Dashboard', but actual {dashboard_title}"

            #Perform logout and validate logout is success or not
            hp.perform_logout()
            assert lp.get_login_header() == 'Login', f"Logout failed. Expected title: Login, but actual {lp.get_login_header}"

        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print(f"Caught {type(e).__name__} and error is : {e}")

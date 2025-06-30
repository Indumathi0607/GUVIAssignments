from selenium.common import ElementNotInteractableException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By


class LoginActions:
    # Method to navigate to Login screen
    def get_into_login_webpage(self, driver):
        try:
            driver.find_element(By.XPATH, "//a[@id='login-btn']").click()
        except (ElementNotInteractableException, NoSuchElementException) as e:
            print("Unable to click on Login.", e)
            assert False, "Login option not found in GUVI home page"

    # Method to validate given textbox is enabled and is displayed
    def validate_input_textbox(self, label_text, textbox_locator, element):
        try:
            assert label_text == element, f"expected: 'Email Address', but actual {label_text}"
            assert textbox_locator.is_displayed(), f"{element} input text box is not displayed"
            assert textbox_locator.is_enabled(), f"{element} input text box is not enabled"

        except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException) as e:
            print(f"Caught {e} with {element}")

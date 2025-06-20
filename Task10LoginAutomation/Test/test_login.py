from selenium.webdriver.common.by import By
from Test.conftest import webpage_info


def perform_login(driver, username, password):
    # Enter username and password and click on login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()

def assert_error_message(driver, expected_msg):
    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert expected_msg in error_msg
    print(f"Warning shown for incorrect credentials {error_msg}")


#Test case to verify login success for valid password
def test_login_with_valid_credentials_success(setup): #Ssetup from fixtures is used
    driver=setup

    perform_login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.XPATH, "//div[@class='bm-burger-button']")

    #add the url after login to the global dict
    webpage_info['url_after_login'] = driver.current_url

    #Fetch the content of the webpage
    webpage_text = driver.find_element(By.TAG_NAME, "body").text
    print(f"Complete text of the webpage after successful login: {webpage_text}")

    #Write the web page content into Webpage_task_10,txt using utf-8,
    # utf-8 will make sure all types of characters (like emojis, symbols, or non-English text) are saved and displayed correctly
    with open("Webpage_task_10.txt", "w", encoding="utf-8") as file:
        file.write(webpage_text)


#Test case to verify login fails for invalid username
def test_whether_login_with_invalid_username_fails(setup):
    driver = setup
    perform_login(driver, "std_user", "secret_sauce")
    assert_error_message(driver, "Username and password do not match any user in this service")

#Test case to verify login fails for invalid password
def test_whether_login_with_invalid_password_fails(setup):
    driver = setup
    perform_login(driver,"standard_user", "secret")
    assert_error_message(driver,"Username and password do not match any user in this service")

#Test to verify login is not possible without username/password
def test_login_fails_with_empty_username(setup):
    #verify empty username is not allowed
    setup.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
    assert_error_message(setup, "Username is required")

# Test to verify login is not possible without username/password
def test_login_fails_with_empty_password(setup):
    #verify empty password is not allowed
    setup.find_element(By.ID, "user-name").send_keys("standard_user")
    setup.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
    assert_error_message(setup, "Password is required")
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException, \
    TimeoutException
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.read_test_data_file import ReadTestDataCSV
from utils.write_test_data_file import WriteInTestDataCSV


class TestLogin:


    @pytest.mark.parametrize("username, password, expected_condition", ReadTestDataCSV.read_csv_data())
    def test_login(self, driver, username, password, expected_condition):

        global test_result
        try:
            lp = LoginPage(driver)
            lp.perform_login(username, password)

            dp = DashboardPage(driver)

            if expected_condition != "":
                actual_error = lp.get_login_error_message()
                assert actual_error == expected_condition, f"Expected error: {expected_condition}, but actual: {actual_error}"

            else:
                assert dp.is_dashboard_displayed() == True, f"Dashboard page is not loaded"

            test_result = "Pass"

        except (NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException, TimeoutException) as e:
            test_result = "Fail"
            pytest.fail(f"Test failed due to Selenium exception: {e}")

        finally:
            WriteInTestDataCSV.write_test_result(username, password, expected_condition, test_result)


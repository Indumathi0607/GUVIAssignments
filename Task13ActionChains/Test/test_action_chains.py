from selenium.common import MoveTargetOutOfBoundsException, NoSuchElementException, TimeoutException, \
    ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTask13ActionChains:

    # Method to validate the text of draggable and droppable elements
    def validate_element_text(self, element, message, expected_text):
            actual_text = element.text
            print(f'{message} : {actual_text}')
            assert actual_text == expected_text, f"Expected test: {expected_text}, but the actual text is: {actual_text}"

    # Method to return the draggable element
    def get_element(self, driver, element_locator, element_name):
        try:
            return WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, element_locator))
            )
        except (TimeoutException, NoSuchElementException) as e:
            print(f"{element_name} is not found. The following exception captured {type(e).__name__} and error is: {e}")
            assert False, f"The {element_name} is not found"

    # Validate draggable element and its text
    def test_draggable_element(self, setup):
        driver = setup
        try:
            draggable_element = self.get_element(driver, "draggable", "Draggable element")
            self.validate_element_text(draggable_element, 'Draggable element text', 'Drag me to my target')
        except NoSuchElementException as e:
            print(f"{e}: Draggable element not found")

    # Validate droppable element and its text
    def test_droppable_element(self, setup):
        driver = setup
        try:
            droppable_element = self.get_element(driver, "droppable", "Droppable element")
            self.validate_element_text(droppable_element, 'Droppable element text', 'Drop here')
        except NoSuchElementException as e:
            print(f"{e}: Droppable element not found")

    # 1. Perform drag and drop using drag and drop
    def test_drag_and_drop_success(self, setup):
        driver = setup
        try:
            draggable_element = self.get_element(driver, "draggable", "Draggable element")
            droppable_element = self.get_element(driver, "droppable", "Droppable element")

            # Perform drag and drop using action chains
            action = ActionChains(driver)
            action.drag_and_drop(draggable_element, droppable_element).perform()

            # Validate droppable text after drag and drop.
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[text() =  'Dropped!']"))
            )
            self.validate_element_text(droppable_element, 'Droppable element text after drag and drop', 'Dropped!')

        except StaleElementReferenceException as e:
            print(f"{e}: Text of Droppable box after drop got stale/refreshed.")
            assert False, "Timeout while waiting for droppable and draggable elements"

    # 2. Perform drag and drop using click_and_hold and move_to_element
    def test_drag_and_drop_success_through_mouse_actions(self, setup):
        driver = setup

        try:
            draggable_element = self.get_element(driver, "draggable", "Draggable element")
            droppable_element = self.get_element(driver, "droppable", "Droppable element")

            # Perform drag and drop using mouse actions
            action = ActionChains(driver)
            action.click_and_hold(draggable_element)
            action.pause(2)
            action.move_to_element(droppable_element)
            action.release().perform()

            # Validate droppable text after drag and drop.
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[text() =  'Dropped!']"))
            )
            self.validate_element_text(droppable_element, 'Droppable element text after drag and drop', 'Dropped!')

        except (ElementNotInteractableException, StaleElementReferenceException) as e:
            print(f"Caught error {type(e).__name__} and the error is {e}")
            assert False, f"Test failed due to {e}"

    # 3. Perform drag and drop using drag_and_drop_by_offset
    def test_drop_at_wrong_location_fails(self, setup):

        driver = setup
        try:
            draggable_element = self.get_element(driver, "draggable", "Draggable element")

            # drag and drop by offset
            ActionChains(driver).drag_and_drop_by_offset(draggable_element, 50, 50).perform()

            droppable_element = self.get_element(driver, "droppable", "Droppable element")
            print("Droppable element text: ", droppable_element.text.strip())
            assert droppable_element.text.strip() != "Dropped!", f"Dropped! message shown even for dropping at wrong location"

        except MoveTargetOutOfBoundsException as e:
            print("MoveTargetOutOfBoundsException caught: ", e)
            assert False, "Test failed due to the element was moved to out of bound location"

    # 4. Perform drag and drop using click_and_hold and move_by_offset
    def test_drag_and_drop_using_move_by_offset(self, setup):
        driver = setup

        try:
            # drag and drop using offset
            draggable_element = self.get_element(driver, "draggable", "Draggable element")
            ActionChains(driver).click_and_hold(draggable_element).move_by_offset(150, 50).release().perform()

            # Validate the drop was success or not
            droppable_element = self.get_element(driver, "droppable", "Droppable element")
            print("Droppable element text: ", droppable_element.text.strip())
            assert droppable_element.text.strip() == "Dropped!", f"Drag and drop failed"

        except MoveTargetOutOfBoundsException as e:
            print("MoveTargetOutOfBoundsException caught: ", e)
            assert False, "Test failed due to the element was moved to out of bound location"

    # 5. Perform drag and drop using move_to_element_with_offset
    def test_drag_and_drop_using_element_and_offset(self, setup):
        driver = setup

        try:
            draggable_element = self.get_element(driver, "draggable", "Draggable element")
            droppable_element = self.get_element(driver, "droppable", "Droppable element")

            #Drag and drop using click and hold and move to element with offset
            (ActionChains(driver).click_and_hold(draggable_element)
             .move_to_element_with_offset(droppable_element, 50, 50).release().perform())

            #Validating the droppable text after drop
            droppable_element = self.get_element(driver, "droppable", "Droppable element")
            print("Droppable element text:", droppable_element.text.strip())
            assert droppable_element.text.strip() == "Dropped!", f"Drag and drop failed"

        except MoveTargetOutOfBoundsException as e:
            print("MoveTargetOutOfBoundsException caught: ", e)
            assert False, "Test failed due to the element was moved to out of bound location"

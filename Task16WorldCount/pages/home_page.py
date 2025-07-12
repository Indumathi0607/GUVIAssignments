from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.world_population_title = (By.XPATH, "//img[@alt = 'TheWorldCounts logo-text'][1]")
        self.world_count = (By.XPATH, "//div[@class='counter-ticker is-size-2-mobile']")

    def is_home_page_title_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.world_population_title)
        ).is_displayed()

    def get_world_count(self):
        world_count = self.driver.find_element(*self.world_count)
        return world_count.text

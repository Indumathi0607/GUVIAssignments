from pages.home_page import HomePage


class TestWorldCount:
    def test_world_count(self, driver):
        hp = HomePage(driver)
        hp.is_home_page_title_displayed()
        print("Enter Ctrl+C to stop the printing")

        try:
            while True:
                world_count = hp.get_world_count()
                print(f"Current world count is: {world_count}")

        except KeyboardInterrupt as e:
            print(f"Execution stopped manually. {e}")
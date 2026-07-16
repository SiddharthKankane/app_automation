from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class ProfileScreen(BaseScreen):
    def verify_user_details(self, expected_name: str, expected_email: str):
        self.wait_for_desc(expected_name)
        self.wait_for_desc(expected_email)

    def logout(self):
        self.tap_desc("Logout")

    def navigate_to_home_tab(self):
        self.tap_desc("Home\nTab 1 of 5")

    def navigate_to_search_tab(self):
        self.tap_desc("Search\nTab 2 of 5")

    def navigate_to_favorites_tab(self):
        self.tap_desc("Favorites\nTab 3 of 5")

    def navigate_to_orders_tab(self):
        self.tap_desc("Orders\nTab 4 of 5")
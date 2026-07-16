from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class SearchScreen(BaseScreen):
    def verify_search_screen_loaded(self):
        self.wait_for_desc("Search Food")

    def execute_search(self, query: str):
        search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
        search_field.click()
        search_field.send_keys(query)
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            pass

    def select_food_item_by_name(self, food_name: str):
        self.tap_xpath(f"//android.widget.ImageView[contains(@content-desc, '{food_name}')]")

    def get_all_visible_results_metadata(self) -> list:
        discovered_items = []
        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ScrollView//android.widget.ImageView")
        for card in cards:
            metadata_block = card.get_attribute("content-desc")
            if metadata_block:
                lines = [line.strip() for line in metadata_block.split('\n') if line.strip()]
                if len(lines) >= 3:
                    discovered_items.append({"title": lines[0], "description": lines[1], "price": lines[2]})
        return discovered_items

    def navigate_to_home_tab(self):
        self.force_hide_keyboard()
        self.tap_desc("Home\nTab 1 of 5")

    def navigate_to_favorites_tab(self):
        self.force_hide_keyboard()
        self.tap_desc("Favorites\nTab 3 of 5")

    def navigate_to_orders_tab(self):
        self.force_hide_keyboard()
        self.tap_desc("Orders\nTab 4 of 5")

    def navigate_to_profile_tab(self):
        self.force_hide_keyboard()
        self.tap_desc("Profile\nTab 5 of 5")
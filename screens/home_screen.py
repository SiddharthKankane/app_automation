from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class HomeScreen(BaseScreen):
    def verify_home_screen_loaded(self):
        self.wait_for_desc("BringApp Cafe")

    def get_cart_item_count(self) -> int:
        try:
            badge = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches("^\\d+$")')
            count_str = badge.get_attribute("content-desc")
            return int(count_str) if count_str else 0
        except Exception:
            return 0

    def click_cart_button(self):
        self.tap_xpath("//android.view.View[@resource-id='home_cart_button']/android.widget.Button")

    def filter_by_category(self, category_name: str):
        self.tap_desc(category_name.capitalize())

    def get_all_menu_items(self) -> list:
        items = []
        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ScrollView//android.widget.ImageView")
        for card in cards:
            desc = card.get_attribute("content-desc")
            if desc:
                lines = [line.strip() for line in desc.split('\n') if line.strip()]
                if len(lines) >= 2:
                    items.append({"name": lines[0], "price": lines[1]})
        return items

    def toggle_favorite_for_item(self, item_name: str):
        self.tap_xpath(f"//android.widget.ImageView[starts-with(@content-desc, '{item_name}')]//android.widget.Button[1]")

    def add_item_to_cart(self, item_name: str):
        self.tap_xpath(f"//android.widget.ImageView[starts-with(@content-desc, '{item_name}')]//android.widget.Button[2]")

    def navigate_to_search_tab(self):
        self.tap_desc("Search\nTab 2 of 5")

    def navigate_to_favorites_tab(self):
        self.tap_desc("Favorites\nTab 3 of 5")

    def navigate_to_orders_tab(self):
        self.tap_desc("Orders\nTab 4 of 5")

    def navigate_to_profile_tab(self):
        self.tap_desc("Profile\nTab 5 of 5")
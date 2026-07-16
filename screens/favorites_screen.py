from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class FavoritesScreen(BaseScreen):
    def verify_favorites_screen_loaded(self):
        self.wait_for_desc("My Favorites")

    def get_all_favorite_items(self) -> list:
        items = []
        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, '$')]")
        for card in cards:
            desc = card.get_attribute("content-desc")
            if desc:
                lines = [line.strip() for line in desc.split('\n') if line.strip()]
                if len(lines) >= 2:
                    items.append({"name": lines[0], "price": lines[1]})
        return items

    def remove_item_from_favorites(self, item_name: str):
        self.tap_xpath(f"//android.widget.ImageView[starts-with(@content-desc, '{item_name}')]//android.widget.Button[1]")

    def add_item_to_cart(self, item_name: str):
        self.tap_xpath(f"//android.widget.ImageView[starts-with(@content-desc, '{item_name}')]//android.widget.Button[2]")

    def navigate_to_home_tab(self):
        self.tap_desc("Home\nTab 1 of 5")

    def navigate_to_search_tab(self):
        self.tap_desc("Search\nTab 2 of 5")

    def navigate_to_orders_tab(self):
        self.tap_desc("Orders\nTab 4 of 5")

    def navigate_to_profile_tab(self):
        self.tap_desc("Profile\nTab 5 of 5")
from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class CartScreen(BaseScreen):
    def verify_cart_screen_loaded(self):
        self.wait_for_desc("Your Cart")

    def get_cart_items_details(self) -> list:
        items = []
        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Total:')]")
        for card in cards:
            desc = card.get_attribute("content-desc")
            if desc:
                lines = [line.strip() for line in desc.split('\n') if line.strip()]
                if len(lines) >= 3:
                    items.append({"name": lines[0], "total_price": lines[1].replace("Total: ", ""), "quantity": int(lines[2])})
        return items

    def increase_item_quantity(self, item_name: str):
        self.tap_xpath(f"//android.view.View[starts-with(@content-desc, '{item_name}')]//android.widget.Button[2]")

    def decrease_item_quantity(self, item_name: str):
        self.tap_xpath(f"//android.view.View[starts-with(@content-desc, '{item_name}')]//android.widget.Button[1]")

    def get_checkout_total_price(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Total']/android.view.View[1]")
        return element.get_attribute("content-desc")

    def click_proceed_to_checkout(self):
        self.tap_desc("PROCEED")

    def click_continue_to_buy(self):
        self.tap_desc("Continue to Buy")

    def click_back(self):
        self.tap_xpath("//android.widget.FrameLayout[@pane-title='Your Cart']//android.widget.Button[1]")

    def clear_all_cart_items(self):
        self.tap_xpath("//android.widget.FrameLayout[@pane-title='Your Cart']//android.widget.Button[2]")
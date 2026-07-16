from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class ItemDetailsScreen(BaseScreen):
    def verify_item_details_screen_loaded(self):
        self.wait_for_desc("Description")

    def click_back(self):
        self.tap_desc("Back")

    def get_item_name(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Description']/preceding-sibling::android.view.View[2]")
        return element.get_attribute("content-desc")

    def get_item_price(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Description']/preceding-sibling::android.view.View[1]")
        return element.get_attribute("content-desc")

    def get_item_description(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Description']/following-sibling::android.view.View[1]")
        return element.get_attribute("content-desc")

    def click_add_to_cart(self):
        self.tap_desc("Add to Cart")
from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class ReceiptScreen(BaseScreen):
    def verify_receipt_screen_loaded(self):
        self.wait_for_desc("Receipt")

    def click_back(self):
        self.tap_desc("Back")

    def get_order_number(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Order #')]")
        return element.get_attribute("content-desc")

    def get_receipt_items_details(self) -> list:
        items = []
        lines = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'x ')]")
        for line in lines:
            desc = line.get_attribute("content-desc")
            if desc:
                parts = [part.strip() for part in desc.split('\n') if part.strip()]
                if len(parts) >= 2:
                    items.append({"item_info": parts[0], "price": parts[1]})
        return items

    def get_total_paid_amount(self) -> str:
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Total Paid']/following-sibling::android.view.View[1]")
        return element.get_attribute("content-desc")

    def click_reorder_items(self):
        self.tap_desc("Reorder These Items")
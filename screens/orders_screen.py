from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class OrdersScreen(BaseScreen):
    def verify_orders_screen_loaded(self):
        self.wait_for_desc("My Orders")

    def get_all_orders_history(self) -> list:
        orders = []
        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'Order ORD-')]")
        for card in cards:
            desc = card.get_attribute("content-desc")
            if desc:
                lines = [line.strip() for line in desc.split('\n') if line.strip()]
                if len(lines) >= 3:
                    price_status_split = lines[2].split(' • ')
                    orders.append({
                        "order_id": lines[0].replace("Order ", ""),
                        "timestamp": lines[1],
                        "total_price": price_status_split[0] if len(price_status_split) > 0 else lines[2],
                        "status": price_status_split[1] if len(price_status_split) > 1 else ""
                    })
        return orders

    def select_order_by_id(self, order_id: str):
        self.tap_xpath(f"//android.widget.Button[contains(@content-desc, 'Order {order_id}')]")

    def navigate_to_home_tab(self):
        self.tap_desc("Home\nTab 1 of 5")

    def navigate_to_search_tab(self):
        self.tap_desc("Search\nTab 2 of 5")

    def navigate_to_favorites_tab(self):
        self.tap_desc("Favorites\nTab 3 of 5")

    def navigate_to_profile_tab(self):
        self.tap_desc("Profile\nTab 5 of 5")
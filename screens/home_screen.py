from screens.base_screen import BaseScreen

class HomeScreen(BaseScreen):
    def verify_home_page_loaded(self):
        self.wait_for_desc("All Menu")

    def navigate_to_profile(self):
        self.tap_desc("Profile\nTab 5 of 5")

    def add_first_item_to_cart(self):
        # Clicks the add button for the Classic Cheeseburger
        self.tap_id("add_to_cart_button_b1")

    def navigate_to_cart(self):
        # Clicks the cart icon in the top right
        self.tap_id("home_cart_button")

    def favorite_classic_cheeseburger(self):
        # Clicks the heart icon based on the ID from the XML
        self.tap_id("fav_button_b1")

    def navigate_to_favorites_tab(self):
        # Uses the exact content-desc from your bottom navigation bar
        self.tap_desc("Favorites\nTab 3 of 5")
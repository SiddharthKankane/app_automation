from screens.base_screen import BaseScreen

class CartScreen(BaseScreen):
    def verify_on_cart_page(self):
        """Verifies the Cart page header is visible."""
        self.wait_for_desc("Your Cart")

    def proceed_to_checkout(self):
        self.tap_desc("PROCEED")
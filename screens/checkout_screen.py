from screens.base_screen import BaseScreen

class CheckoutScreen(BaseScreen):
    def confirm_and_place_order(self):
        # We use xpath here to be safe and catch the text/desc combination
        self.tap_xpath("//*[contains(@content-desc, 'Confirm & Place Order') or contains(@text, 'Confirm & Place Order')]")
from screens.base_screen import BaseScreen

class TrackOrderScreen(BaseScreen):
    def verify_order_is_delivered(self):
        # Waits for the text to appear signaling the animation finished
        self.wait_for_desc("Order Delivered!")

    def return_to_home(self):
        self.tap_desc("Back to Home")
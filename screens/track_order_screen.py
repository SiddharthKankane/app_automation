from screens.base_screen import BaseScreen

class TrackOrderScreen(BaseScreen):
    def verify_track_order_screen_loaded(self):
        self.wait_for_desc("Track Order")

    def is_order_placed_step_displayed(self) -> bool:
        return self.is_displayed_xpath("//android.view.View[@content-desc='Order Placed']")

    def is_preparing_step_displayed(self) -> bool:
        return self.is_displayed_xpath("//android.view.View[@content-desc='Preparing']")

    def is_on_the_way_step_displayed(self) -> bool:
        return self.is_displayed_xpath("//android.view.View[@content-desc='On the Way']")

    def is_order_delivered_step_displayed(self) -> bool:
        return self.is_displayed_xpath("//android.view.View[@content-desc='Delivered']")

    def click_back_to_home(self):
        """Attempts to click 'Back to Home'. Falls back to standard back navigation or bottom tabs."""
        try:
            # Attempt 1: Look for an explicit "Back to Home" button (by content-desc or text)
            self.tap_xpath("//*[@content-desc='Back to Home' or @text='Back to Home']")
        except Exception:
            print("[WARN] 'Back to Home' button not found. Attempting top-left back arrow...")
            try:
                # Attempt 2: Click the standard Android top-left back arrow
                self.tap_xpath("//android.widget.Button[@content-desc='Back' or contains(@content-desc, 'Navigate up')]")
            except Exception:
                # Attempt 3: If all else fails, use the physical Android back key!
                print("[WARN] UI Back arrow failed. Sending physical Android BACK keycode.")
                self.driver.press_keycode(4)
from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class CheckoutScreen(BaseScreen):
    def verify_checkout_screen_loaded(self):
        self.wait_for_desc("Checkout Details")

    def enter_delivery_instructions(self, instructions: str):
        input_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
        input_field.click()
        input_field.send_keys(instructions)
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            pass

    def open_payment_method_options(self):
        self.tap_xpath("//android.widget.Button[contains(@content-desc, 'Cash on Delivery')]")

    def select_payment_method(self, method_type: str):
        self.open_payment_method_options()
        normalized_method = method_type.lower()
        if "cash" in normalized_method:
            self.tap_desc("Cash on Delivery")
        elif "credit" in normalized_method or "card" in normalized_method:
            self.tap_desc("Credit Card")
        elif "upi" in normalized_method:
            self.tap_desc("UPI")

    def click_confirm_and_place_order(self):
        self.tap_desc("Confirm & Place Order")

    def dismiss_payment_options_modal(self):
        self.tap_desc("Dismiss")

    def click_back(self):
        self.tap_xpath("//android.widget.Button[1]")
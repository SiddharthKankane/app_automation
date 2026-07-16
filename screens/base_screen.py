from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def tap_desc(self, description):
        element = self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, description)))
        element.click()

    def force_hide_keyboard(self):
        """Bulletproof method to close the Android keyboard using multiple strategies."""
        try:
            # Strategy 1: Check if keyboard is shown, then use Appium's built-in hide
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            pass

        # Strategy 2: If Strategy 1 failed and the keyboard is STILL up, press the Android Back key!
        try:
            if self.driver.is_keyboard_shown():
                print("[WARN] Standard hide_keyboard failed. Using Android BACK key to dismiss keyboard.")
                self.driver.press_keycode(4)  # Keycode 4 is the Android physical BACK button
        except Exception:
            # Fallback for some drivers where press_keycode fails
            try:
                self.driver.back()
            except Exception:
                pass

    def fill_id(self, resource_id, text):
        element = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, resource_id)))
        element.click()
        element.clear()
        element.send_keys(text)

        self.force_hide_keyboard()


    def fill_xpath(self, xpath, text):
        element = self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, xpath)))
        element.click()
        element.clear()
        element.send_keys(text)

        self.force_hide_keyboard()

    def wait_for_desc(self, description):
        self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, description)))

    def scroll_forward(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )

    def get_toast_message(self):
        """Captures the text of a temporary Android toast message."""
        # Android exposes all toast messages to this exact XPath
        toast_xpath = "//android.widget.Toast"

        try:
            # We use a shorter wait time (5 seconds) because toasts disappear quickly
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_xpath))
            )
            return element.text
        except TimeoutException:
            return None

    def tap_id(self, resource_id):
        """Click an element using its resource-id."""
        element = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, resource_id)))
        element.click()

    def tap_xpath(self, xpath):
        """Click an element using its XPath."""
        element = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
        element.click()

    def is_displayed_xpath(self, xpath):
        """Checks if an element is present and displayed, returns boolean."""
        try:
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            return element.is_displayed()
        except TimeoutException:
            return False
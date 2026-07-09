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

    def fill_id(self, resource_id, text):
        element = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, resource_id)))
        element.send_keys(text)

    def fill_xpath(self, xpath, text):
        element = self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, xpath)))
        element.click()
        element.clear()
        element.send_keys(text)

        # Safely hide the keyboard after typing
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            # If the keyboard is already hidden or the command isn't supported, just move on
            pass

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
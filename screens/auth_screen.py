from screens.base_screen import BaseScreen


class AuthScreen(BaseScreen):
    def register_user(self, username, email, phone, location, password, confirm_password):
        self.tap_desc("Register\nTab 2 of 2")

        # Using XPath with triple quotes to safely handle all the weird symbols
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_username_field'>]"]""", username)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_email_field'>]"]""", email)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_phone_field'>]"]""", phone)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_location_field'>]"]""", location)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_password_field'>]"]""", password)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'register_confirm_password_field'>]"]""",
                        confirm_password)

        self.scroll_forward()
        self.tap_desc("Register")

    def verify_duplicate_user_error(self):
        """Verifies the 'already exists' toast message appears."""
        toast_text = self.get_toast_message()

        # If it returns None, the toast never appeared
        assert toast_text is not None, "The duplicate user error toast did not appear!"

        # Verify the text matches exactly what is in your screenshot
        assert toast_text == "Username already exists!", f"Expected 'Username already exists!', but got: '{toast_text}'"

    def login_user(self, username, password):
        self.tap_desc("Login\nTab 1 of 2")
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'login_username_field'>]"]""", username)
        self.fill_xpath("""//android.widget.EditText[@resource-id="[<'login_password_field'>]"]""", password)
        self.tap_desc("Login")

    def verify_invalid_login_error(self):
        """Verifies the 'Invalid username or password!' toast message appears."""
        toast_text = self.get_toast_message()

        # If it returns None, the toast never appeared
        assert toast_text is not None, "The invalid login error toast did not appear!"

        # Verify the text matches exactly what is in your screenshot
        assert toast_text == "Invalid username or password!", f"Expected 'Invalid username or password!', but got: '{toast_text}'"
from screens.base_screen import BaseScreen

class ProfileScreen(BaseScreen):
    def verify_user_details(self, expected_name, expected_email):
        self.wait_for_desc(expected_name)
        self.wait_for_desc(expected_email)

    def logout(self):
        self.tap_desc("Logout")
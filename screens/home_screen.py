from screens.base_screen import BaseScreen

class HomeScreen(BaseScreen):
    def verify_home_page_loaded(self):
        self.wait_for_desc("All Menu")

    def navigate_to_profile(self):
        self.tap_desc("Profile\nTab 5 of 5")
from screens.base_screen import BaseScreen

class FavoritesScreen(BaseScreen):
    def verify_on_favorites_page(self):
        """Verifies the header of the Favorites page is visible."""
        self.wait_for_desc("My Favorites")

    def verify_item_is_favorited(self, item_name="Classic Cheeseburger"):
        """Checks if the specific item card is displayed in the list."""
        xpath = f"//android.widget.ImageView[contains(@content-desc, '{item_name}')]"
        return self.is_displayed_xpath(xpath)

    def add_item_to_cart(self, item_name="Classic Cheeseburger"):
        """Taps the yellow '+' button for the specified item."""
        # In the XML, the '+' button is the 2nd button inside the item's ImageView
        # XPath uses 1-based indexing, so Button[2] targets the second button
        xpath = f"//android.widget.ImageView[contains(@content-desc, '{item_name}')]/android.widget.Button[2]"
        self.tap_xpath(xpath)

    def navigate_to_cart(self):
        """Taps the Cart icon in the top right header."""
        # Finds the 'My Favorites' header text, moves up to the parent container, and selects the Button (Cart Icon)
        xpath = "//android.view.View[@content-desc='My Favorites']/../android.widget.Button"
        self.tap_xpath(xpath)
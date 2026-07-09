import pytest


def test_end_to_end_order_flow(app, test_data):
    """Verifies a user can log in, add an item to the cart, and successfully checkout."""
    user = test_data["valid_user"]

    # 1. Login Flow
    app.auth.login_user(user["name"], user["password"])

    # Wait for the main menu to appear so we know login was successful
    app.home.verify_home_page_loaded()

    # 2. Shopping Flow
    app.home.add_first_item_to_cart()
    app.home.navigate_to_cart()

    # 3. Cart & Checkout Flow
    app.cart.proceed_to_checkout()
    app.checkout.confirm_and_place_order()

    # 4. Tracking & Validation
    app.track_order.verify_order_is_delivered()
    app.track_order.return_to_home()

    # 5. Verify we made it back to the beginning of the loop
    app.home.verify_home_page_loaded()
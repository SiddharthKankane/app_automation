def test_happy_path_direct_login_and_complete_e2e_checkout_flow(app, existing_user_data):

    user = existing_user_data["valid_user"]
    target_item = "Classic Cheeseburger"

    # 1. Direct login bypass operation using previously captured account values
    app.auth.login_user(user["name"], user["password"])
    app.home.verify_home_screen_loaded()

    # 2. Search & Select targeted food items assets
    app.home.navigate_to_search_tab()
    app.search.verify_search_screen_loaded()
    app.search.execute_search(target_item)
    app.search.select_food_item_by_name(target_item)

    # 3. Add to shopping cart from specific item details view context
    app.item_details.verify_item_details_screen_loaded()
    assert app.item_details.get_item_name() == target_item
    app.item_details.click_add_to_cart()
    app.item_details.click_back()

    # 4. Route back to Home screen to launch the central order basket
    app.search.navigate_to_home_tab()
    app.home.click_cart_button()
    app.cart.verify_cart_screen_loaded()

    items_in_cart = app.cart.get_cart_items_details()
    assert any(item["name"] == target_item for item in items_in_cart)
    app.cart.click_proceed_to_checkout()

    # 5. Populate checkout forms and select billing pipeline options
    app.checkout.verify_checkout_screen_loaded()
    app.checkout.enter_delivery_instructions("Please drop it at the front porch.")
    app.checkout.select_payment_method("Cash on Delivery")
    app.checkout.click_confirm_and_place_order()

    # 6. Parse confirmation values generated out of post-purchase view state
    app.track_order.click_back_to_home()
    app.home.navigate_to_orders_tab()
    app.orders.verify_orders_screen_loaded()


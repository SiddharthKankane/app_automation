def test_complete_registration_login_profile_and_logout_flow(app, new_user_data):
    """Happy Path: Verifies registration with fresh data, logging in,
    navigating to profile details, and successfully logging out."""

    # 1. Extract fresh data generated and saved to users.json
    user = new_user_data["valid_user"]

    # 2. Fresh Registration Flow (Archives old data automatically)
    app.auth.register_user(
        username=user["name"],
        email=user["email"],
        phone=user["phone"],
        location=user["location"],
        password=user["password"],
        confirm_password=user["confirm_password"]
    )

    # 3. Login Flow with the newly registered data
    app.auth.login_user(username=user["name"], password=user["password"])
    app.home.verify_home_screen_loaded()

    # 4. Profile Navigation & Verification
    app.home.navigate_to_profile_tab()
    app.profile.verify_user_details(expected_name=user["name"], expected_email=user["email"])

    # 5. Teardown / Session Termination
    app.profile.logout()
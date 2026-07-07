# tests/test_profile.py
from faker import Faker

def test_user_registration_and_login_flow(app, test_data):
    """Happy Path: Verifies a user can register, log in, view profile, and log out."""
    # 1. Load Test Data from the fixture
    user = test_data["valid_user"]

    # 2. Register Flow
    app.auth.register_user(
        user["name"],
        user["email"],
        user["phone"],
        user["location"],
        user["password"],
        user["confirm_password"]
    )

    # 3. Login Flow
    app.auth.login_user(user["name"], user["password"])

    # 4. Navigation and Assertions
    app.home.verify_home_page_loaded()
    app.home.navigate_to_profile()

    app.profile.verify_user_details(user["name"], user["email"])

    # 5. Teardown
    app.profile.logout()



def test_invalid_login_is_blocked(app):
    """Negative Path: Verifies fake credentials trigger the correct toast error."""
    fake = Faker()

    unregistered_username = fake.user_name() + "_invalid"
    wrong_password = fake.password(length=12)

    app.auth.login_user(
        username=unregistered_username,
        password=wrong_password
    )
    app.auth.verify_invalid_login_error()
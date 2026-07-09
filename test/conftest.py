import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from screens.auth_screen import AuthScreen
from screens.home_screen import HomeScreen
from screens.profile_screen import ProfileScreen
from screens.cart_screen import CartScreen
from screens.checkout_screen import CheckoutScreen
from screens.track_order_screen import TrackOrderScreen
from screens.favorites_screen import FavoritesScreen
import json
from utils.data_manager import generate_and_archive_user


# ==========================================
# 1. COMMAND LINE OPTIONS
# ==========================================
def pytest_addoption(parser):
    """Adds a custom command line argument to select the environment."""
    parser.addoption(
        "--env",
        action="store",
        default="browserstack",
        help="Environment to run tests against: emulator, physical, or browserstack"
    )


# ==========================================
# 2. DATA FIXTURE
# ==========================================

@pytest.fixture(scope="function")
def test_data():
    """Provides test data (either custom from file or dynamically generated)."""
    return get_test_data()

# ==========================================
# 3. DYNAMIC DRIVER FIXTURE
# ==========================================
@pytest.fixture(scope="function")
def app_driver(request):
    """Configures the driver based on the --env flag."""

    # Get the environment flag from the terminal command
    env = request.config.getoption("--env").lower()

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.app_package = "com.example.food_app"
    options.app_activity = ".MainActivity"

    # ----------------------------------------
    # Route 1: Local Emulator
    # ----------------------------------------
    if env == "emulator":
        print("\n🚀 Routing test to Local Emulator...")
        # Optional: Specify exact emulator if multiple are running
        # options.udid = "emulator-5554"
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    # ----------------------------------------
    # Route 2: Physical Device
    # ----------------------------------------
    elif env == "physical":
        print("\n📱 Routing test to Physical Device...")
        # Best practice: Pull UDID from an environment variable so it isn't hardcoded
        device_udid = os.environ.get("PHYSICAL_DEVICE_UDID", "00078347E000323")
        options.udid = device_udid
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    # ----------------------------------------
    # Route 3: BrowserStack (Cloud)
    # ----------------------------------------
    elif env == "browserstack":
        print("\n☁️ Routing test to BrowserStack...")
        bs_username = os.environ.get("BROWSERSTACK_USERNAME", "your_username")
        bs_access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY", "your_access_key")
        app_url = os.environ.get("BROWSERSTACK_APP_URL", "bs://your_uploaded_app_hash")

        bstack_options = {
            "userName": bs_username,
            "accessKey": bs_access_key,
            "deviceName": "Samsung Galaxy S23 Ultra",
            "osVersion": "13.0",
            "app": app_url,
            "projectName": "BringApp E2E",
            "buildName": "Android Regression v1.0",
            "local": "false",
            "debug": "true",
            "networkLogs": "true"
        }

        options.load_capabilities({"bstack:options": bstack_options})
        hub_url = "https://hub-cloud.browserstack.com/wd/hub"
        driver = webdriver.Remote(command_executor=hub_url, options=options)

    else:
        raise ValueError(f"Unknown environment: {env}. Please use emulator, physical, or browserstack.")

    # Yield the configured driver to the test
    yield driver

    # Teardown
    driver.quit()


# ==========================================
# 4. APP PAGE OBJECTS FIXTURE
# ==========================================
@pytest.fixture(scope="function")
def app(app_driver):
    class AppScreens:
        auth = AuthScreen(app_driver)
        home = HomeScreen(app_driver)
        profile = ProfileScreen(app_driver)
        cart = CartScreen(app_driver)
        checkout = CheckoutScreen(app_driver)
        track_order = TrackOrderScreen(app_driver)

    return AppScreens()
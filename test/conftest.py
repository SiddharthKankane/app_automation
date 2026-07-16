import os
import json
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Base & Authentication Screens
from screens.auth_screen import AuthScreen
from screens.profile_screen import ProfileScreen

# Core Dashboard & Item Discovery Screens
from screens.home_screen import HomeScreen
from screens.search_screen import SearchScreen
from screens.item_details_screen import ItemDetailsScreen
from screens.favorites_screen import FavoritesScreen

# Cart & Order Transaction Management
from screens.cart_screen import CartScreen
from screens.checkout_screen import CheckoutScreen

# Post-Purchase & Tracking Screens
from screens.receipt_screen import ReceiptScreen
from screens.track_order_screen import TrackOrderScreen
from screens.orders_screen import OrdersScreen

# Data Flow Utility Helpers
from utils.data_manager import get_existing_user, get_new_user


# ==========================================
# 1. COMMAND LINE OPTIONS
# ==========================================
def pytest_addoption(parser):
    """Adds a custom command line argument to select the environment."""
    parser.addoption(
        "--env",
        action="store",
        default="physical",
        help="Environment to run tests against: emulator, physical, or browserstack"
    )


# ==========================================
# 2. DATA FIXTURES (UPDATED)
# ==========================================

@pytest.fixture(scope="function")
def new_user_data():
    """Archives old data and generates brand new user data. Use for fresh registration flows."""
    return get_new_user()


@pytest.fixture(scope="function")
def existing_user_data():
    """Reads existing user data without creating a new user or wiping profiles. Use for direct login flows."""
    return get_existing_user()


# ==========================================
# 3. DYNAMIC DRIVER FIXTURE
# ==========================================
@pytest.fixture(scope="session")
def app_driver(request):
    """Configures the driver based on the --env flag."""

    # Get the environment flag from the terminal command
    env = request.config.getoption("--env").lower()

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.app_package = "com.example.food_app"
    options.app_activity = ".MainActivity"
    options.no_reset = True
    options.full_reset = False

    # ----------------------------------------
    # Route 1: Local Emulator
    # ----------------------------------------
    if env == "emulator":
        print("\n🚀 Routing test to Local Emulator...")
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    # ----------------------------------------
    # Route 2: Physical Device
    # ----------------------------------------
    elif env == "physical":
        print("\n📱 Routing test to Physical Device...")
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

    yield driver
    driver.quit()



# 4. APP PAGE OBJECTS FIXTURE
# ==========================================
# ==========================================
@pytest.fixture(scope="function")
def app(app_driver):
    class AppScreens:
        # Authentication & Onboarding
        auth = AuthScreen(app_driver)

        # Dashboard & Discovery
        home = HomeScreen(app_driver)
        search = SearchScreen(app_driver)
        item_details = ItemDetailsScreen(app_driver)
        favorites = FavoritesScreen(app_driver)

        # Cart & Transaction Pipeline
        cart = CartScreen(app_driver)
        checkout = CheckoutScreen(app_driver)

        # Post-Purchase Fulfillment & History
        receipt = ReceiptScreen(app_driver)
        track_order = TrackOrderScreen(app_driver)
        orders = OrdersScreen(app_driver)

        # Account Management
        profile = ProfileScreen(app_driver)

    return AppScreens()
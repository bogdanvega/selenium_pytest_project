import pytest

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config
from utils.test_data import TEST_VALID_USER_1, TEST_INVALID_USER


@pytest.mark.parametrize("email, password, should_login, date_of_birth", [
        (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_19),
        (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False, Config.AGE_19)
])
def test_free_shipping_when_order_over_20(driver, email, password, should_login, date_of_birth):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        assert login_page.is_visible_logout_button()
        driver.back()
        checkout_page = CheckoutPage(driver).load()
        checkout_page.remove_all_items_from_cart()
        shop_page = ShopPage(driver).load()
        assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.add_product_to_cart("gala apples")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        checkout_page.load()
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.click_plus_button(Config.BUTTON_PLUS_QUANTITY[10])
        assert float(checkout_page.get_product_total()) > Config.MIN_PRODUCT_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_total()) < Config.MIN_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_shipment()) == Config.FREE_SHIPMENT
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


@pytest.mark.parametrize("email, password, should_login, date_of_birth", [
        (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_19),
        (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False, Config.AGE_19)
])
def test_shipping_cost_when_order_just_below_20(driver, email, password, should_login, date_of_birth):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        assert login_page.is_visible_logout_button()
        driver.back()
        checkout_page = CheckoutPage(driver).load()
        checkout_page.remove_all_items_from_cart()
        shop_page = ShopPage(driver).load()
        assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.add_product_to_cart("pink lady apples")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        shop_page.add_product_to_cart("birchwood quarter pounders")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        checkout_page.load()
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.click_plus_button("pink lady apples", Config.BUTTON_PLUS_QUANTITY[6])
        assert float(checkout_page.get_product_total()) < Config.MIN_PRODUCT_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_total()) < Config.MIN_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_shipment()) > Config.FREE_SHIPMENT
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


@pytest.mark.parametrize("email, password, should_login, date_of_birth", [
        (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_19),
        (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False, Config.AGE_19)
])
def test_free_shipping_cost_is_not_kept(driver, email, password, should_login, date_of_birth):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        assert login_page.is_visible_logout_button()
        driver.back()
        checkout_page = CheckoutPage(driver).load()
        checkout_page.remove_all_items_from_cart()
        shop_page = ShopPage(driver).load()
        assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.add_product_to_cart("ginger")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        shop_page.add_product_to_cart("large flat mushrooms")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        checkout_page.load()
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.click_plus_button("large flat mushrooms", Config.BUTTON_PLUS_QUANTITY[17])
        assert float(checkout_page.get_product_total()) > Config.MIN_PRODUCT_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_total()) < Config.MIN_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_shipment()) == Config.FREE_SHIPMENT
        checkout_page.click_minus_button("large flat mushrooms", Config.BUTTON_PLUS_QUANTITY[1])
        assert float(checkout_page.get_product_total()) < Config.MIN_PRODUCT_TOTAL_FOR_FREE_SHIPMENT
        assert float(checkout_page.get_total()) < Config.MIN_TOTAL_FOR_FREE_SHIPMENT
        assert int(checkout_page.get_shipment()) > Config.FREE_SHIPMENT
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE

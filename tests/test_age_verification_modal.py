import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config
from utils.test_data import TEST_VALID_USER_1, TEST_INVALID_USER


@pytest.mark.parametrize("email, password, should_login", [
        (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True),
        (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False)
])
def test_modal_is_displayed(driver, email, password, should_login):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        assert login_page.is_visible_logout_button()
        driver.back()
        shop_page = ShopPage(driver).load()
        assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


@pytest.mark.parametrize("date_of_birth", [
    Config.AGE_18
])
def test_user_18_years_old_can_view_alcoholic_products(driver, date_of_birth):
    HomePage(driver).load()
    shop_page = ShopPage(driver).load()
    assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
    shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
    assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
    shop_page.view_category_products("alcohol")
    assert shop_page.get_first_product_name() != ""


@pytest.mark.parametrize("date_of_birth", [
    Config.AGE_17
])
def test_user_17_years_old_cannot_view_alcoholic_products(driver, date_of_birth):
    HomePage(driver).load()
    shop_page = ShopPage(driver).load()
    assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
    shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
    assert shop_page.get_error_message() == Config.UNDERAGE_MESSAGE
    shop_page.view_category_products("alcohol")
    assert shop_page.get_underage_notice_text() == Config.UNDERAGE_NOTICE_TEXT


@pytest.mark.parametrize("date_of_birth", [
    Config.AGE_20_INVALID_DATE_FORMAT,
    Config.EMPTY_BIRTH_DATE
])
def test_invalid_date_birth_format(driver, date_of_birth):
    HomePage(driver).load()
    shop_page = ShopPage(driver).load()
    assert shop_page.get_age_modal_text() == Config.AGE_MODAL_TEXT
    shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
    assert shop_page.get_error_message() == Config.WRONG_FORMAT_MESSAGE
    shop_page.view_category_products("alcohol")
    assert shop_page.get_underage_notice_text() == Config.UNDERAGE_NOTICE_TEXT

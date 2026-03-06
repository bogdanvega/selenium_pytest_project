import time

from pages.shop_page import ShopPage


def test_shop_add_oranges_to_cart(driver):
    shop_page = ShopPage(driver)
    shop_page.load()
    time.sleep(2)
    shop_page.enter_date_age_modal("23-10-1990")
    shop_page.confirm_age_modal()
    time.sleep(2)
    shop_page.add_to_cart()
    shop_page.add_to_favourites()
    shop_page.open_auth_profile_by_icon()

from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from utils.config import Config

class ShopPage(HomePage):
    """
    Page object for the shop page.
    """
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class = 'modal-content']/input[@type = 'text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class = 'modal-content']/button[text() = 'Confirm']")
    CONFIRMATION_MSG = (By.XPATH, "//div[@role = 'status']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")
    QUANTITY_INPUT = (By.XPATH, f"//div[@class = 'product-card']//input[@type = 'number'][{Config.ITEM_NUMBER}]")
    ADD_TO_CART_BUTTON = (By.XPATH, f"//button[@class = 'btn btn-primary btn-cart'][{Config.ITEM_NUMBER}]")
    ADD_TO_FAVORITES_BUTTON = (By.XPATH, f"//button[@class = 'btn btn-outline-dark '][{Config.ITEM_NUMBER}]")
    CATEGORY_FILTER_LIST = (By.XPATH, f"//h4[@class = 'widget-title']/following-sibling::ul/li[{Config.CATEGORY}]")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        return self.open(Config.SHOP_PAGE_URL)

    def enter_date_age_modal(self, date):
        self.type_text(self.AGE_VERIFICATION_INPUT, date)
        return self

    def confirm_age_modal(self):
        self.click(self.AGE_VERIFICATION_CONFIRM_BUTTON)

    def get_confirmation_message(self):
        if self.is_visible(self.CONFIRMATION_MSG):
            return self.get_text(self.CONFIRMATION_MSG)
        return None

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return None

    def enter_quantity_input(self, quantity):
        self.type_text(self.QUANTITY_INPUT, quantity)
        return self

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def add_to_favourites(self):
        self.click(self.ADD_TO_FAVORITES_BUTTON)

    def select_category_list(self):
        self.click(self.CATEGORY_FILTER_LIST)

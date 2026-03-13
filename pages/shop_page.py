from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from utils.config import Config

ADD_TO_CART_BUTTON = {
    "celery": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[2]/button"),
    "cauliflower": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/button"),
    "asparagus": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/button")
}

ADD_TO_FAVOURITE_BUTTON = {
    "celery": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[3]/button")
}

PRODUCT_INFO = {
    "celery": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[1]"),
    "gala_apples": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[10]/div/div[1]"),
    "kale": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[3]/div/div[1]"),
    "cauliflower": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]"),
    "asparagus": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]")
}

PAGE_BUTTON = {
    "2": (By.XPATH, "//button[@class = 'pagination-link' and text() = '2']"),
    "3": (By.XPATH, "//button[@class = 'pagination-link' and text() = '3']"),
    "4": (By.XPATH, "//button[@class = 'pagination-link' and text() = '4']")
}

RATING_STARS = {
    "1": (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[1]"),
    "2": (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[2]"),
    "3": (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[3]"),
    "4": (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[4]"),
    "5": (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[5]")
}

QUANTITY_INPUT_PRODUCT = {
    "celery": (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/input")
}

class ShopPage(HomePage):
    """
    Page object for the shop page.
    """
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class = 'modal-content']/input[@type = 'text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class = 'modal-content']/button[text() = 'Confirm']")
    CONFIRMATION_MSG = (By.XPATH, "//div[@role = 'status']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")
    QUANTITY_INPUT_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/input")
    COMMENT_INPUT = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/textarea")
    SEND_RATING_BUTTON = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[3]/button[2]")
    COMMENT_OPTIONS = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div[1]")
    COMMENT_TEXT = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/p")
    DELETE_COMMENT = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div[2]/button[2]")
    RATING_RESTRICTION = (By.XPATH, "//*[@id='root']/div/section/div[3]/p")
    RATING_USER = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/h5/strong")
    CUSTOM_RATING = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[2]/div/div/div[1]/span[contains(@class,'full')]")
    CATEGORY_FILTER_LIST = (By.XPATH, f"//h4[@class = 'widget-title']/following-sibling::ul/li[{Config.ALL_CATEGORY}]")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Next']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Previous']")

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

    def enter_quantity_input(self, quantity, product):
        if product not in QUANTITY_INPUT_PRODUCT:
            raise ValueError(f"Unknown product: {product}")
        self.type_text(QUANTITY_INPUT_PRODUCT[product], quantity)
        return self

    def add_product_to_cart(self, product):
        if product not in ADD_TO_CART_BUTTON:
            raise ValueError(f"Unknown product: {product}")
        self.scroll_into_view(ADD_TO_CART_BUTTON[product])
        self.click(ADD_TO_CART_BUTTON[product])

    def add_to_favourites(self, product):
        if product not in ADD_TO_FAVOURITE_BUTTON:
            raise ValueError(f"Unknown product: {product}")
        self.scroll_into_view(ADD_TO_FAVOURITE_BUTTON[product])
        self.click(ADD_TO_FAVOURITE_BUTTON[product])

    def select_category_list(self):
        self.scroll_into_view(self.CATEGORY_FILTER_LIST)
        self.click(self.CATEGORY_FILTER_LIST)

    def next_page(self):
        self.scroll_into_view(self.NEXT_PAGE_BUTTON)
        self.click(self.NEXT_PAGE_BUTTON)

    def previous_page(self):
        self.scroll_into_view(self.PREVIOUS_PAGE_BUTTON)
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def page(self, page_number):
        self.scroll_into_view(PAGE_BUTTON[page_number])
        self.click(PAGE_BUTTON[page_number])

    def view_product_info(self, product):
        self.scroll_into_view(PRODUCT_INFO[product])
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(PRODUCT_INFO[product])).click()

    def rate_stars(self, stars):
        self.click(RATING_STARS[stars])

    def comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    def send_rating(self):
        self.click(self.SEND_RATING_BUTTON)

    def delete_rating(self):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.COMMENT_OPTIONS)
        ).click()

        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.DELETE_COMMENT)
        ).click()

        self.wait_and_accept_alert()

        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.invisibility_of_element_located(self.COMMENT_OPTIONS)
        )

    def has_existing_rating(self, username):
        users = self.driver.find_elements(*self.RATING_USER)

        for user in users:
            if user.text.lower() == username.lower():
                return True
        return False

    def get_rating_restriction_text(self):
        return self.get_text(self.RATING_RESTRICTION)

    def get_rating_user(self):
        return self.get_text(self.RATING_USER)

    def get_rating(self):
        rating = self.find_all(self.CUSTOM_RATING)
        return len(rating)

    def get_comment_text(self):
        return self.get_text(self.COMMENT_TEXT)

    def wait_for_confirmation_message(self, text):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(self.CONFIRMATION_MSG, text)
        )

    def wait_for_confirmation_to_disappear(self):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.invisibility_of_element(self.CONFIRMATION_MSG)
        )

    def wait_for_user_rating(self, username):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(self.RATING_USER, username.capitalize()
            )
        )

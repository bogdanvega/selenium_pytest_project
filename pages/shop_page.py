from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from utils.config import Config

ADD_TO_CART_BUTTON = {
    "celery": (By.XPATH, "//img[@alt='Celery']/following::button[@class = 'btn btn-primary btn-cart']"),
    "cauliflower": (By.XPATH, "//img[@alt='Cauliflower']/following::button[@class = 'btn btn-primary btn-cart']"),
    "asparagus": (By.XPATH, "//img[@alt='Asparagus']/following::button[@class = 'btn btn-primary btn-cart']")
}

ADD_TO_FAVOURITE_BUTTON = {
    "celery": (By.XPATH, "//img[@alt='Celery']/following::button[@class = 'btn btn-outline-dark ']")
}

PRODUCT_INFO = {
    "celery": (By.XPATH, "//img[@alt='Celery']"),
    "gala_apples": (By.XPATH, "//img[@alt='Gala Apples']"),
    "kale": (By.XPATH, "//img[@alt='Kale']"),
    "cauliflower": (By.XPATH, "//img[@alt='Cauliflower']"),
    "asparagus": (By.XPATH, "//img[@alt='Asparagus']")
}

PAGE_BUTTON = {
    "2": (By.XPATH, "//button[@class = 'pagination-link' and text() = '2']"),
    "3": (By.XPATH, "//button[@class = 'pagination-link' and text() = '3']"),
    "4": (By.XPATH, "//button[@class = 'pagination-link' and text() = '4']")
}

RATING_STARS = {
    "1": (By.XPATH, "//div[@class = 'interactive-rating']/span[1]"),
    "2": (By.XPATH, "//div[@class = 'interactive-rating']/span[2]"),
    "3": (By.XPATH, "//div[@class = 'interactive-rating']/span[3]"),
    "4": (By.XPATH, "//div[@class = 'interactive-rating']/span[4]"),
    "5": (By.XPATH, "//div[@class = 'interactive-rating']/span[5]")
}

QUANTITY_INPUT_PRODUCT = {
    "celery": (By.XPATH, "//img[@alt='Celery']/following::input[@type = 'number']")
}

class ShopPage(HomePage):
    """
    Page object for the shop page.
    """
    # --- AGE VERIFICATION ---
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class = 'modal-content']/input[@type = 'text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class = 'modal-content']/button[text() = 'Confirm']")

    CONFIRMATION_MSG = (By.XPATH, "//div[@role = 'status']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")

    # --- RATING SYSTEM ---
    COMMENT_INPUT = (By.XPATH, "//textarea[@class = 'new-review-form-control ']")
    SEND_RATING_BUTTON = (By.XPATH, "//button[@class = 'new-review-btn new-review-btn-send']")
    COMMENT_OPTIONS = (By.XPATH, "//div[@class = 'menu-icon']")
    COMMENT_TEXT = (By.XPATH, "//div[@class = 'comment'][1]/div[@class = 'comment-body']//p")
    EDIT_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[1]")
    DELETE_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[2]")
    RATING_RESTRICTION = (By.XPATH, "//div[@class = 'reviewRestriction']/p")
    RATING_USER = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'comment-header']//strong")
    CUSTOM_RATING = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'custom-rating']/span[@class = 'star full']")

    # --- PAGINATION ---
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
        locator = ADD_TO_CART_BUTTON.get(product)
        if not locator:
            raise ValueError(f"Unknown product: {product}")
        self.scroll_into_view(ADD_TO_CART_BUTTON[product])
        self.click(ADD_TO_CART_BUTTON[product])

    def add_to_favourites(self, product):
        if product not in ADD_TO_FAVOURITE_BUTTON:
            raise ValueError(f"Unknown product: {product}")
        self.scroll_into_view(ADD_TO_FAVOURITE_BUTTON[product])
        self.click(ADD_TO_FAVOURITE_BUTTON[product])

    def next_page(self):
        self.scroll_into_view(self.NEXT_PAGE_BUTTON)
        self.click(self.NEXT_PAGE_BUTTON)

    def previous_page(self):
        self.scroll_into_view(self.PREVIOUS_PAGE_BUTTON)
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def page(self, page_number):
        locator = PAGE_BUTTON.get(page_number)
        if not locator:
            raise ValueError(f"Invalid page number: {page_number}")
        self.scroll_into_view(locator)
        self.click(locator)

    def view_product_info(self, product):
        self.scroll_into_view(PRODUCT_INFO[product])
        self.wait.until(EC.visibility_of_element_located(PRODUCT_INFO[product])).click()

    def rate_stars(self, stars):
        self.click(RATING_STARS[stars])

    def comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    def send_rating(self):
        self.click(self.SEND_RATING_BUTTON)

    def delete_rating(self):
        self.wait.until(
            EC.element_to_be_clickable(self.COMMENT_OPTIONS)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_COMMENT)
        ).click()

        self.wait_and_accept_alert()

        self.wait.until(
            EC.invisibility_of_element_located(self.COMMENT_OPTIONS)
        )

    def has_existing_rating(self, username):
        user = self.get_rating_user()
        if user.lower() == username.lower():
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
        self.wait.until(
            EC.text_to_be_present_in_element(self.CONFIRMATION_MSG, text)
        )

    def wait_for_confirmation_to_disappear(self):
        self.wait.until(
            EC.invisibility_of_element(self.CONFIRMATION_MSG)
        )

    def wait_for_user_rating(self, username):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RATING_USER, username.capitalize()
            )
        )

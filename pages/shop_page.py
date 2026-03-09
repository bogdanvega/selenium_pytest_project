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
    QUANTITY_INPUT_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/input")
    ADD_TO_CART_BUTTON_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[2]/button")
    ADD_TO_FAVORITES_BUTTON_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[3]/button")
    PRODUCT_INFO_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]")
    CELERY_RATING_4_STARS = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[4]")
    CELERY_COMMENT = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/textarea")
    CELERY_SEND_RATING_BUTTON = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[3]/button[2]")
    CELERY_COMMENT_OPTIONS = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div")
    CELERY_DELETE_COMMENT = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div[2]/button[2]")
    CELERY_RATING_RESTRICTION = (By.XPATH, "//*[@id='root']/div/section/div[3]/p")
    CELERY_RATING_USER = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/h5/strong")
    CELERY_CUSTOM_RATING = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[2]/div/div/div[1]/span[contains(@class,'full')]")

    CATEGORY_FILTER_LIST = (By.XPATH, f"//h4[@class = 'widget-title']/following-sibling::ul/li[{Config.ALL_CATEGORY}]")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Next']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Previous']")
    PAGE_BUTTON_2 = (By.XPATH, "//button[@class = 'pagination-link' and text() = '2']")


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

    def enter_quantity_input_celery(self, quantity):
        self.type_text(self.QUANTITY_INPUT_CELERY, quantity)
        return self

    def add_to_cart_celery(self):
        self.click(self.ADD_TO_CART_BUTTON_CELERY)

    def add_to_favourites_celery(self):
        self.click(self.ADD_TO_FAVORITES_BUTTON_CELERY)

    def select_category_list(self):
        self.click(self.CATEGORY_FILTER_LIST)

    def next_page(self):
        self.click(self.NEXT_PAGE_BUTTON)

    def previous_page(self):
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def page_2(self):
        self.click(self.PAGE_BUTTON_2)

    def view_product_info_celery(self):
        self.click(self.PRODUCT_INFO_CELERY)

    def rate_celery_4_stars(self):
        self.click(self.CELERY_RATING_4_STARS)

    def comment_celery(self):
        self.type_text(self.CELERY_COMMENT, "Fresh")

    def send_rating_celery(self):
        self.click(self.CELERY_SEND_RATING_BUTTON)

    def delete_rating_celery(self):
        self.click(self.CELERY_COMMENT_OPTIONS)
        self.click(self.CELERY_DELETE_COMMENT)
        self.wait_and_accept_alert()

    def get_celery_rating_restriction_text(self):
        return self.get_text(self.CELERY_RATING_RESTRICTION)

    def get_celery_rating_user(self):
        return self.get_text(self.CELERY_RATING_USER)

    def get_celery_rating(self):
        rating = self.find_all(self.CELERY_CUSTOM_RATING)
        return len(rating)
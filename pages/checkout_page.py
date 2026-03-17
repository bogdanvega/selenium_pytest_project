from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.config import Config

MINUS_BUTTON = {
    "gala apples": (By.XPATH, "//h5[text() = 'Gala Apples']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'minus']"),
    "pink lady apples" : (By.XPATH, "//h5[text() = 'Pink Lady Apples']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'minus']"),
    "large flat mushrooms": (By.XPATH, "//h5[text() = 'Large Flat Mushrooms']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'minus']"),
    "celery": (By.XPATH, "//h5[text() = 'Celery']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'minus']")
}

PLUS_BUTTON = {
    "gala apples": (By.XPATH, "//h5[text() = 'Gala Apples']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'plus']"),
    "pink lady apples" : (By.XPATH, "//h5[text() = 'Pink Lady Apples']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'plus']"),
    "large flat mushrooms": (By.XPATH, "//h5[text() = 'Large Flat Mushrooms']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'plus']"),
    "celery": (By.XPATH, "//h5[text() = 'Celery']/ancestor::div[@class = 'checkout-card-item-container']//button[@class = 'plus']")
}

class CheckoutPage(BasePage):
    """
    Page object for the checkout/cart page.
    """
    SHIPMENT_VALUE = (By.XPATH, "//h5[text()='Shipment:']/following-sibling::h5")
    PRODUCT_TOTAL = (By.XPATH, "//h5[text()='Product Total:']/following-sibling::h5")
    TOTAL_VALUE = (By.XPATH, "//h5[text()='Total:']/following-sibling::h5")
    REMOVE_ITEM = (By.XPATH, "//a[@class = 'remove-icon']")
    STREET_FIELD = (By.XPATH, "//input[@name = 'street']")
    CITY_FIELD = (By.XPATH, "//input[@name = 'city']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@name = 'postalCode']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@name = 'cardNumber']")
    NAME_ON_CARD_FIELD = (By.XPATH, "//input[@name = 'nameOnCard']")
    EXPIRATION_CARD_FIELD = (By.XPATH, "//input[@name = 'expiration']")
    CVV_CARD_FIELD = (By.XPATH, "//input[@name = 'cvv']")
    BUY_NOW_BUTTON = (By.XPATH, "//button[@class = 'btn-buy-now']")


    def __init__(self, driver):
        super().__init__(driver)

    # -- ACTIONS --
    def load(self):
        return self.open(Config.CHECKOUT_PAGE_URL)

    def enter_street(self, street):
        self.type_text(self.STREET_FIELD, street)
        return self

    def enter_city(self, city):
        self.type_text(self.CITY_FIELD, city)
        return self

    def enter_postal_code(self, postal_code):
        self.type_text(self.POSTAL_CODE_FIELD, postal_code)
        return self

    def enter_card_number(self, card_number):
        self.type_text(self.CARD_NUMBER_FIELD, card_number)
        return self

    def enter_name_on_card(self, name_on_card):
        self.type_text(self.NAME_ON_CARD_FIELD, name_on_card)
        return self

    def enter_expiration_card(self, expiration_card):
        self.type_text(self.EXPIRATION_CARD_FIELD, expiration_card)
        return self

    def enter_cvv_card(self, cvv_card):
        self.type_text(self.CVV_CARD_FIELD, cvv_card)
        return self

    def buy_now(self):
        self.click(self.BUY_NOW_BUTTON)

    def click_minus_button(self, product, nr_of_times):
        locator = MINUS_BUTTON[product]
        for i in range(nr_of_times):
            self.click(locator)

    def click_plus_button(self, product, nr_of_times):
        locator = PLUS_BUTTON[product]
        for i in range(nr_of_times):
            self.click(locator)

    def get_shipment(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SHIPMENT_VALUE)
        )
        return element.text.strip().replace("€", "")

    def get_product_total(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_TOTAL)
        )
        return element.text.strip().replace("€", "")

    def get_total(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_VALUE)
        )
        return element.text.strip().replace("€", "")

    def remove_all_items_from_cart(self):
        while True:
            buttons = self.driver.find_elements(*self.REMOVE_ITEM)
            if not buttons:
                break
            buttons[0].click()
            self.wait.until(
                EC.staleness_of(buttons[0])
            )

    def is_visible_buy_now_button(self):
        return self.is_visible(self.BUY_NOW_BUTTON)

    def complete_checkout(self, street, city, postal_code, card_number, name_on_card, expiration, cvv):
        self.enter_street(street)
        self.enter_city(city)
        self.enter_postal_code(postal_code)
        self.enter_card_number(card_number)
        self.enter_name_on_card(name_on_card)
        self.enter_expiration_card(expiration)
        self.enter_cvv_card(cvv)
        self.buy_now()


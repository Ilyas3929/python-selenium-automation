from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="search"][data-test="@web/Search/SearchButton"]')
    CART_EMPTY_MSG = (By.XPATH, '//h1[text()="Your cart is empty"]')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(9)

    def empty_cart_text(self):
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        expected_text = "Your cart is empty"
        assert expected_text in actual_text, f'Error. Expected text is: {expected_text} Actual text is: {actual_text}'
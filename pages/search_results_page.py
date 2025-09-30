from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    PRODUCT_MSG = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')

    def verify_search_results(self, product):
        actual_text = self.find_element(*self.PRODUCT_MSG).text
        assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'
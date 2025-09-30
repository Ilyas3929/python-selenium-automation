from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_MSG = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@then("Verify “Your cart is empty” message is shown")
def empty_cart_text(context):
    context.app.empty_cart_text.verify_search_results()


@then("Verify {product} is in the cart")
def added_product(context, product):
    context.app.search_results_page.verify_search_results()
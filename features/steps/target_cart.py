from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_EMPTY_MSG = (By.XPATH, '//h1[text()="Your cart is empty"]')
PRODUCT_MSG = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@then("Verify “Your cart is empty” message is shown")
def empty_cart_text(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    expected_text = "Your cart is empty"
    assert expected_text in actual_text, f'Error. Expected text is: {expected_text} Actual text is: {actual_text}'


@then("Verify {product} is in the cart")
def added_product(context, product):
    actual_text = context.driver.find_element(*PRODUCT_MSG).text
    assert product in actual_text, f'Error. Expected text is: {product} Actual text is: {actual_text}'
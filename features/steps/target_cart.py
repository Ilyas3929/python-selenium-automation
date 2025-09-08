
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page")
def open_main(context):
    context.driver.get("https://www.target.com/")

@when("Cart is empty")
def cart_navigation(context):
    context.driver.find_element(By.XPATH, '//div[@data-test="@web/CartIcon"]').click()
    sleep(5)

@then("Verify “Your cart is empty” message is shown")
def empty_cart_text(context):
    actual_text = context.driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text
    expected_text = "Your cart is empty"
    assert expected_text in actual_text, f'Error. Expected text is: {expected_text} Actual text is: {actual_text}'
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, "search")
SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="search"][data-test="@web/Search/SearchButton"]')
CART_ICON = (By.XPATH, '//div[@data-test="@web/CartIcon"]')


@when("Search for {product}")
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    sleep(1)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(1)


@when("Adding product to the cart")
def add_to_cart(context):
    ADD_BUTTON = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor94582690")
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ADD_BUTTON)
    sleep(1)
    ADD_BUTTON.click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()
    sleep(4)
    CLOSE_BUTTON = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="close"][type="button"]')
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", CLOSE_BUTTON)
    sleep(1)
    context.driver.execute_script("arguments[0].click();", CLOSE_BUTTON)


@when("Clicking on cart icon")
def cart_navigation(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(4)
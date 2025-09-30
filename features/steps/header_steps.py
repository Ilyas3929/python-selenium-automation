from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, "search")
SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="search"][data-test="@web/Search/SearchButton"]')
CART_ICON = (By.XPATH, '//div[@data-test="@web/CartIcon"]')


@when("Search for {product}")
def search_product(context, product):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_FIELD))
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON))
    context.driver.find_element(*SEARCH_BUTTON).click()


@when("Adding product to the cart")
def add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.ID, "addToCartButtonOrTextIdFor94582690")))
    ADD_BUTTON = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor94582690")
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ADD_BUTTON)
    ADD_BUTTON.click()

    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="orderPickupButton"]')))
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()

    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="close"][type="button"]')))
    CLOSE_BUTTON = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="close"][type="button"]')
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", CLOSE_BUTTON)
    context.driver.execute_script("arguments[0].click();", CLOSE_BUTTON)


@when("Clicking on cart icon")
def cart_navigation(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-test="@web/CartIcon"]')),
                      message="Cart icon is not clickable")
    context.driver.find_element(*CART_ICON).click()
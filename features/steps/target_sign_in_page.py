from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("User is clicking on the Account icon")
def main_menu_account_button(context):
 context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')))
 context.driver.find_element(By.XPATH, '//span[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]').click()


@when("User is clicking on Sign in from the right side navigation menu")
def right_side_navigation_sign_in_button(context):
 context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="accountNav-signIn"]')))
 context.driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()


@then("Sign in form is openned")
def sign_in_form_is_openned_verification(context):
 context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Sign in with passkey"]')))
 actual_text = context.driver.find_element(By.XPATH, '//button[text()="Sign in with passkey"]').text
 expected_text = 'Sign in with passkey'
 assert expected_text in actual_text, f'The sign in form is openned'

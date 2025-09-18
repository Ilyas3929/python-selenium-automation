from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://www.target.com/"
driver.get(url)
driver.maximize_window()


driver.find_element(By.ID, "search").send_keys("Tazo Strawberry Matcha Latte Sweetened Green Tea Concentrate - 32 fl oz")
sleep(1)
driver.find_element(By.CSS_SELECTOR, '[aria-label="search"][data-test="@web/Search/SearchButton"]').click()
sleep(4)


ADD_BUTTON = driver.find_element(By.ID, "addToCartButtonOrTextIdFor94582690")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ADD_BUTTON)
sleep(1)
ADD_BUTTON.click()
sleep(4)
driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()
sleep(4)

CLOSE_BUTTON = driver.find_element(By.CSS_SELECTOR, '[aria-label="close"][type="button"]')
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", CLOSE_BUTTON)
sleep(1)
driver.execute_script("arguments[0].click();", CLOSE_BUTTON)

driver.find_element(By.XPATH, '//div[@data-test="@web/CartIcon"]').click()
sleep(5)

actual_text = driver.find_element(By.CSS_SELECTOR,'[data-test="cartItem-title"]').text
expected_text = "Tazo Strawberry Matcha Latte Sweetened Green Tea Concentrate - 32 fl oz"
assert expected_text in actual_text, f'Error. Expected text is: {expected_text} Actual text is: {actual_text}'

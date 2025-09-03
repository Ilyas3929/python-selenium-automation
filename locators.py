from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://amazon.com/"
driver.get(url)
driver.maximize_window()

#Navigating to the sign-in page
driver.find_element(By.ID, 'nav-link-accountList').click()
sleep(4)

#Amazon logo
driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]').click()
sleep(4)

driver.back()
sleep(4)

#Email field
driver.find_element(By.ID, 'ap_email_login').send_keys('test123@gmail.com')
sleep(4)
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-close"]').click()
sleep(4)

#Continue button
driver.find_element(By.XPATH, '//input[@class="a-button-input"]').click()
sleep(4)

#Conditions of use link
driver.find_element(By.XPATH,  '//a[text()="Conditions of Use"]').click()
sleep(4)
driver.back()

#Privacy Notice link
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]').click()
sleep(4)
driver.back()

#Need help link
original_tab = driver.current_window_handle
driver.find_element(By.XPATH, '//div[@class="a-section"]//a[@role="button"]').click()
sleep(4)
driver.switch_to.window(original_tab)

#Forgot your password link
driver.find_element(By.ID, 'ap_email_login').send_keys('test123@gmail.com')
sleep(4)
driver.find_element(By.XPATH, '//input[@class="a-button-input"]').click()
sleep(4)
driver.find_element(By.ID, 'auth-fpp-link-bottom').click()
sleep(4)

#Other issues with Sign-In link
#The Sign-In link is no longer available on the web page

#Create your Amazon account button
#The Create your Amazon account button is no longer available on the web page




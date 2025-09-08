from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements

driver = webdriver.Chrome()
url = "https://amazon.com/"
driver.get(url)
driver.maximize_window()

#Navigating to the sign-in page
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList').click()
sleep(2)

#Clicking on the email field and entering the email
driver.find_element(By.CSS_SELECTOR, '#ap_email_login').send_keys("test123@gmail.com")
sleep(2)

#Clicking on the Continue button
driver.find_element(By.CSS_SELECTOR, '.a-button-input').click()
sleep(2)

#Clicking on the password field and inserting an incorrect data
driver.find_element(By.CSS_SELECTOR, '#ap_password').send_keys("Q")
sleep(2)

#Clicking on the sign in button
driver.find_element(By.CSS_SELECTOR, '#signInSubmit').click()
sleep(2)
driver.back()
sleep(2)
driver.back()
sleep(2)

#Conditions of use link
driver.find_element(By.XPATH,  '//a[text()="Conditions of Use"]').click()
sleep(2)
driver.back()

#Privacy Notice link
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]').click()
sleep(2)
driver.back()

#Clicking on the "Need help?" link
driver.find_element(By.CSS_SELECTOR, '[target="_blank"].a-size-base').click()
sleep(2)
driver.back()
sleep(2)








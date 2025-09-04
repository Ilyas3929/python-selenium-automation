from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#1. Practice with locators.

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

#2. Create a test case for the SignIn page using python & selenium script.

#Open https://www.target.com/
driver.get("https://www.target.com/")

#Click Account button
driver.find_element(By.XPATH, '//span[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]').click()
sleep(4)

#Click SignIn btn from side navigation
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()
sleep(4)

'''
Verify SignIn page opened: 
“Sign in or create account” text is shown,
SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
'''
actual_text = driver.find_element(By.XPATH, '//button[text()="Sign in with passkey"]').text
print(actual_text)

'''
[Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), 
make sure it works and you remember selenium commands.
'''
driver.get("https://www.target.com/")
sleep(4)
driver.find_element(By.ID, 'search').send_keys("Jeans")
driver.find_element(By.XPATH, '//button[@aria-label="search"]').click()
sleep(4)

driver.quit()



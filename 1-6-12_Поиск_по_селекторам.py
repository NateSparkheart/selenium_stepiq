from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")

first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
first_name.send_keys("Alexandr")

last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
last_name.send_keys("Pushkin")

email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
email.send_keys("moroz_i_solnce@gmai.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
assert "Congratulations! You have successfully registered!" == welcome_text_element.text

time.sleep(10)
browser.quit()
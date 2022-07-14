import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys("Nate")
last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys("Sparkheart")
email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys("kappa@.com")

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
bio_path = os.path.join(current_dir, 'Bio.txt') # добавляем к этому пути имя файла

file_attacher = browser.find_element(By.ID, "file").send_keys(bio_path)

submit_button = browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(15)
browser.quit()
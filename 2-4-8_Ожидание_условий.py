import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element(By.ID, "book").click()

x = browser.find_element(By.ID, "input_value").text
answer_area = browser.find_element(By.ID, "answer").send_keys(math.log(abs(12*math.sin(int(x)))))

solve_button = browser.find_element(By.ID, "solve").click()

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
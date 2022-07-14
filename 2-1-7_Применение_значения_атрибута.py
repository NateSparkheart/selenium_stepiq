from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome() # задаем инструмент для работы с браузером
browser.get("http://suninjuly.github.io/get_attribute.html") # указываем ссылку для инструмента
time.sleep(2)

treasurebox = browser.find_element(By.TAG_NAME, "img") # выбираем элемент
value_x = treasurebox.get_attribute("valuex") # из выбранного элемента считываем значение определенного атрибута

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

answer_area = browser.find_element(By.ID, "answer")
answer_area.send_keys(calc(value_x))
time.sleep(2)

robobox = browser.find_element(By.ID, "robotCheckbox").click()
time.sleep(2)

robobutton = browser.find_element(By.ID, "robotsRule").click()
time.sleep(2)

submit_button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(10)
browser.quit()
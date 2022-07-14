from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button_1st = browser.find_element(By.TAG_NAME, "button").click()

alert = browser.switch_to.alert # переход на модальное окно
alert.accept()

# alert.dismiss - это отмена
# alert.send_keys("My answer") - это вставка ответа в поле подтверждения
# prompt.accept()/dismiss()

x = browser.find_element(By.ID, "input_value").text

answer_area = browser.find_element(By.ID, "answer").send_keys(math.log(abs(12*math.sin(int(x)))))

submit_button = browser.find_element(By.TAG_NAME, "button").click()
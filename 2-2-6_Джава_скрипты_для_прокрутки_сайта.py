import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_value = browser.find_element(By.ID, "input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

answer_area = browser.find_element(By.ID, "answer")
browser.execute_script('return arguments[0].scrollIntoView(true);', answer_area)
answer_area.send_keys(calc(x_value))

robobox = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script('return arguments[0].scrollIntoView(true);', robobox)
robobox.click()

robobutton = browser.find_element(By.ID, "robotsRule")
browser.execute_script('return arguments[0].scrollIntoView(true);', robobutton)
robobutton.click()

submit_button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script('return arguments[0].scrollIntoView(true);', submit_button)
submit_button.click()

time.sleep(15)
browser.quit()

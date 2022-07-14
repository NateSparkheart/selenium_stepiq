from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element(By.TAG_NAME, "button").click()

browser.switch_to.window(browser.window_handles[1])

x = browser.find_element(By.ID, "input_value").text

answer_area = browser.find_element(By.ID, "answer").send_keys(math.log(abs(12*math.sin(int(x)))))

submit_button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(15)
browser.quit()

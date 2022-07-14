import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

sum = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)

select_area = Select(browser.find_element(By.TAG_NAME, "select"))
select_area.select_by_visible_text(str(sum))

submit_button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(5)
browser.quit()


import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

# robot_radio = browser.find_element(By.ID, "robotsRule")
#
# robot_checked = robot_radio.get_attribute("checked")
#
# print("value of robot radio: ", robot_checked)
#
# assert robot_checked is not None, "Robot radio is not selected by default"
people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

time.sleep(15)
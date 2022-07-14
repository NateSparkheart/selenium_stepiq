from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegistration(unittest.TestCase):
    def test_form_1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
        first_name.send_keys("Viktor")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
        last_name.send_keys("Korneplod")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
        email.send_keys("kartoshka25@gmail.com")
        button = browser.find_element(By.TAG_NAME, "button").click()
        comfirmation_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", comfirmation_text,
                         "Ёбаный рот этого казино!")

    def test_form_2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your name']")
        first_name.send_keys("Viktor")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
        last_name.send_keys("Korneplod")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
        email.send_keys("kartoshka25@gmail.com")
        button = browser.find_element(By.TAG_NAME, "button").click()
        comfirmation_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", comfirmation_text,
                         "Ёбаный рот этого казино!")

if __name__ == "__main__":
    unittest.main()
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

def form_test(link): # проверка формы регистрации, на вход линк
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[class='form-control first']").send_keys("Viktor")
    browser.find_element(By.CSS_SELECTOR, "[placeholder ='Input your last name']").send_keys("Korneplod")
    browser.find_element(By.CSS_SELECTOR, "[class='form-control third']").send_keys("kartoshka25@gmail.com")
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    return browser.find_element(By.TAG_NAME, "h1").text

class TestReg(unittest.TestCase):
    def test_form_1(self):
        self.assertEqual(form_test("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!",
                         "***ный рот этого казино!")

    def test_form_2(self):
        self.assertEqual(form_test("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!",
                         "***ный рот этого казино!")

if __name__ == "__main__":
    unittest.main()





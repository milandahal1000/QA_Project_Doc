import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("I am before setup")
    #
    # def tearDown(self):
    #     print("I am after setup")
    #
    # def test_a(self):
    #     print("I am test a")
    #
    # def test_b(self):
    #     print("I am test b")

    # @classmethod
    # def setUpClass(self) -> None:
    #     print("I am before setup")
    #
    # @classmethod
    # def tearDownClass(self):
    #     print("I am after setup")
    #
    # def test_a(self):
    #     print("I am test a")
    #
    # def test_b(self):
    #     print("I am test b")

    def setUp(self):
        self.driver = webdriver.Chrome()  # opens chrome
        self.driver.maximize_window()  # maximize the window
        self.driver.get('https://www.demoblaze.com/')  # opens the linked site

    def test_login(self):
        driver = self.driver
        nav_login = driver.find_element("id", "login2")
        nav_login.click()
        driver.implicitly_wait(10)
        txt_box = driver.find_element(By.ID, "loginusername")
        txt_box.send_keys("testmorning")
        txt_password = driver.find_element(By.ID, "loginpassword")
        txt_password.send_keys("test123")
        login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()
        time.sleep(5)
        expected_result = "Welcome testmorning"
        actual_result = driver.find_element(By.ID,'nameofuser').text
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()

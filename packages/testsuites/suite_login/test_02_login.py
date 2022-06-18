import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class test_02_login(unittest.TestCase): # pylint: disable=invalid-name
    """"foo"""
    def setUp(self):

        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(10)

    def test_02(self):
        """this function Passing invalid email and password"""
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("rose22@gmail.com")
        passwd = self.driver.find_element(By.NAME, "pass")
        passwd.send_keys("tyhsuuy")
        passwd.send_keys(Keys.RETURN)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

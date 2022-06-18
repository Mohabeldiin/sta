import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_01_login(unittest.TestCase):
    """foo"""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(10)
        
    def test_01(self):
        """this function Passing vaild email and blank password"""
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("lol@gmail.com")
        passwd = self.driver.find_element(By.NAME, "pass")
        passwd.send_keys(" ")
        passwd.send_keys(Keys.RETURN)
    
    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()
            
if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
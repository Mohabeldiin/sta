"""this test case Check all the optional fields when do not fill data
    TC_04_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_04_Registration(unittest.TestCase):
    """1- Do not enter any detail in optional fields.
       2- Enter valid data in required fields.
       3- Click on the Signup button"""
    
    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()


    def test_01_Optional_Fields(self):
        """Check all the optional fields when do not fill data"""
        pass


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()

if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
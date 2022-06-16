"""this test case Check user should Register by filling all the required fields
    TC_03_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_03_Registration(unittest.TestCase):
    """1- Enter valid values in the required fields.
       2- Click on the Register button."""
    
    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()


    def test_01_Required_fields(self):
        """Check user should Register by filling all the required fields"""
        pass


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()

if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
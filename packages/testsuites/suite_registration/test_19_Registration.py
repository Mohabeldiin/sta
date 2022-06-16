"""this test case foo
    TC_foo_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_Data(object):
    """this class is enum holds the test data that is used in this test case"""
    pass


class Test_foo_Registration(unittest.TestCase):
    """foo\n
    1- foo\n
    2- foo"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()

    def test_foo_foo(self):
        """foo\n
        EC: foo"""
        pass

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
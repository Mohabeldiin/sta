"""this test case Check all the valid emails
    TC_07_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_Data(object):
    """this class is enum holds the test data that is used in this test case"""
    EMAIL1 = "test.22@gmail.com"
    EMAIL2 = "test@gmail.com"


class Test_07_Registration(unittest.TestCase):
    """Check all the valid emails.\n
    1- Enter valid Emails.\n
    2- Click on the Register Button."""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        #self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.login_form_locator = (By.CLASS_NAME,"_9vtf")
        self.creat_new_account_locator = (By.ID, "u_0_2_eG")

        try:
            if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_form_locator)
            ).is_displayed():
                self.creat_new_acount = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.creat_new_account_locator)
                )
                self.creat_new_acount.click()
        except: assert False

        self.email_textfiled_locator = (By.NAME,'reg_email__')
        self.confirme_email_textfiled_locator = (By.NAME,'reg_email_confirmation__')
        self.sinUp_button_locator = (By.NAME, "websubmit")
        self.textfiled_mandatory_symbol = (By.CLASS_NAME, "_5dbc img sp_98fCI7IVTTz_1_5x sx_e1ddd6")
        
    def test_01_Email_validation(self):
        """Check the valid email: test.22@gmail.com.\n
        EC: It should not show any validation message."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.send_keys(Test_Data.EMAIL1)
            confirme_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.confirme_email_textfiled_locator)
            )
            confirme_email.send_keys(Test_Data.EMAIL1)
            sinUp_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.sinUp_button_locator)
            )
            sinUp_button.click()
            mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
            )
            if len(mandatory_symbol) == 2:
                assert True
        except AssertionError:
            assert False

    def test_02_Email_validation(self):
        """Check the valid email: test@gmail.com.
        EC: It should not show any validation message."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.send_keys(Test_Data.EMAIL2)
            confirme_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.confirme_email_textfiled_locator)
            )
            confirme_email.send_keys(Test_Data.EMAIL1)
            sinUp_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.sinUp_button_locator)
            )
            sinUp_button.click()
            mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
            )
            if len(mandatory_symbol) == 2:
                assert True
        except AssertionError:
            assert False

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
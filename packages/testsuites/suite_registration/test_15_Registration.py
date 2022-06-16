"""this test case Verify if blank spaces are passed in required fields.
    TC_15_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_Data(object):
    """this class is enum holds the test data that is used in this test case"""
    BLANK_SPACES = " "

class Test_15_Registration(unittest.TestCase):
    """Verify if blank spaces are passed in required fields.\n
    1- Go to the Site.\n
    2- Passed blank spaces in required fields.\n
    3- Click on the Register button.\n"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.login_form_locator = (By.CLASS_NAME,"_9vtf")
        self.creat_new_account_locator = (By.LINK_TEXT, "Create New Account")

        try:
            if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_form_locator)
            ).is_displayed():
                self.creat_new_acount = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.creat_new_account_locator)
                )
                self.creat_new_acount.click()
        except TimeoutException:
            print("\n###############\n",TimeoutException.__doc__ , "\n###############\n")
            assert False

        self.sinUp_button_locator = (By.NAME, "websubmit")
        #self.error_message_locator = (By.ID, '_5633 _5634 _53ij') #js_ub What's your name?  "_5633 _5634 _53ij"
        self.textfiled_mandatory_symbol = (By.CLASS_NAME, "_5dbc img sp_98fCI7IVTTz sx_54513f")

    def test_01_Required_Fields(self):
        """Verify if blank spaces are passed in required fields.\n
        EC: Those Blank spaces should trim and Validation error message for required fields should visible.\n"""
        self.frist_name_textfiled_locator = (By.NAME, 'firstname')
        try:
            try:
                frist_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.frist_name_textfiled_locator)
                )
                frist_name.send_keys(Test_Data.BLANK_SPACES)
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                # error = WebDriverWait(self.driver, 10).until(
                # EC.visibility_of_element_located(self.error_message_locator)
                # )
                # if error:
                #     assert True
                mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
                )
                if len(mandatory_symbol) == 3:
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            except TimeoutException:
                #print("\n###############\n",TimeoutException.__doc__ , "Can't fined error message:", self.error_message_locator , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
            assert False

    def test_02_Required_Fields(self):
        """Verify if blank spaces are passed in required fields.\n
        EC: Those Blank spaces should trim and Validation error message for required fields should visible.\n"""
        self.last_name_textfiled_locator = (By.NAME, 'lastname')
        try:
            try:
                last_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.frist_name_textfiled_locator)
                )
                last_name.send_keys(Test_Data.BLANK_SPACES)
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                # error = WebDriverWait(self.driver, 10).until(
                # EC.visibility_of_element_located(self.error_message_locator)
                # )
                # if error:
                #     assert True
                mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
                )
                if len(mandatory_symbol) == 3:
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            except TimeoutException:
                #print("\n###############\n",TimeoutException.__doc__ , "Can't fined error message:", self.error_message_locator , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
            assert False

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
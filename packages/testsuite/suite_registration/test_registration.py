"""this test case Check the password when passing only numbers
    TC_13_registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


#import unittest
#from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait


class Test_Data(object):
    """this class is enum holds the test data that is used in this test case"""
    PASSWORD = "12345678"


class Test_13_Registration(unittest.TestCase):
    """Check the password when passing only numbers.\n
    1- Enter a value in numbers which is in between 8-32.\n
    2- Click on Register button.
     NOTE:
            This is a Not Applicable Test Case.
            facebook does not have validation message for passing only numbers."""

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

        self.password_textfiled_locator = (By.NAME, 'reg_passwd__')
        self.sinUp_button_locator = (By.NAME, "websubmit")
        self.error_message_locator = (By.ID, "foo")

    #creating 19 test case as test_1_registration
    def test_1_registration(self):
        """foo"""

    def test_2_registration(self):
        """foo"""

    def test_3_registration(self):
        """foo"""

    def test_4_registration(self):
        """foo"""

    def test_5_registration(self):
        """foo"""

    def test_6_registration(self):
        """foo"""

    def test_7_registration(self):
        """foo"""

    def test_8_registration(self):
        """foo"""

    def test_9_registration(self):
        """foo"""

    def test_10_registration(self):
        """foo"""

    def test_11_registration(self):
        """foo"""

    def test_12_registration(self):
        """foo"""

    def test_13_registration(self):
        """Check the password when passing only numbers.\n
            1- Enter a value in numbers which is in between 8-32.\n
            2- Click on Register button."""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.password_textfiled_locator)
                )
                phone.send_keys(Test_Data.PASSWORD)
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                self.driver.find_element()
                sinup = WebDriverWait(self.driver, 10).until(
                    #EC.presence_of_element_located(self.sinUp_button_locator)
                    EC.text_to_be_present_in_element()
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
            assert False

    def test_14_registration(self):
        """foo"""

    def test_15_registration(self):
        """foo"""

    def test_16_registration(self):
        """foo"""

    def test_17_registration(self):
        """foo"""

    def test_18_registration(self):
        """foo"""

    def test_19_registration(self):
        """foo"""

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
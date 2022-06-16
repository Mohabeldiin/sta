"""this test case Check the Email text field that has Email validation
    TC_06_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import enum
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Test_Data(enum.Enum):
    """this class is enum holds the test data that is used in this test case"""
    email_without_at = "testgmail.com"
    email_random = "test@gmail.com"
    email_without_at_in_word = "testAtgmail.com"
    email_without_dot = "test@gmailcom"

class Test_06_Registration(unittest.TestCase):
    """1- Enter Invalid Emails.
       2- Click on the Register Button.
       Description:
                Check the Email text field that has an Email address without @ symbol.
                Check the Email text field that has a random string instead of a real email.
                Check the Email text field that has @ symbol written in words.
                Check the Email text field that has a missing dot in the email address.
        Test Data:
                1.testgmail.com
                2.test@gmail.com
                3.testAtgmail.com
                4.test@gmailcom"""
    
    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.login_form_locator = (By.CLASS_NAME,"_9vtf")
        self.creat_new_account_locator = (By.ID, "u_0_2_Yq")

        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_form_locator)
            )
            self.creat_new_acount = self.driver.find_element(*self.creat_new_account_locator)
            self.creat_new_acount.click()
        except: assert False

        self.email_textfiled_locator = (By.NAME,'reg_email__')
        self.confirme_email_textfiled_locator = (By.NAME,'reg_email_confirmation__')

    def test_01_Email_validation(self):
        """Check the Email text field that has an Email address without @ symbol."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_at)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(self.confirme_email_textfiled_locator)
        except: assert False


    def test_02_Email_validation(self):
        """Check the Email text field that has a random string instead of a real email."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_random)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(self.confirme_email_textfiled_locator)
        except: assert False


    def test_03_Email_validation(self):
        """Check the Email text field that has @ symbol written in words."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_at_in_word)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(self.confirme_email_textfiled_locator)
        except: assert False

    def test_04_Email_validation(self):
        """Check the Email text field that has a missing dot in the email address."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_dot)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(self.confirme_email_textfiled_locator)
        except: assert False


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
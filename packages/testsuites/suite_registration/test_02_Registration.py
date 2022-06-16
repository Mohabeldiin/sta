"""this test case Check the required fields by not filling any data
    TC_02_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Test_02_Registration(unittest.TestCase):
    """1-Do not enter any value in the field.
        2-Click on the Register button."""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_form = (By.CLASS_NAME,"_9vtf")
        self.sinup_button = (By.NAME,"websubmit")
        self.creat_new_account = (By.ID, "u_0_2_Yq")
        self.textfiled_mandatory_symbol = (By.CLASS_NAME, "_5dbc img sp_98fCI7IVTTz_1_5x sx_e1ddd6")
        self.radio_mandatory_symbol = (By.CLASS_NAME, "_5dbc _5k_6 img sp_98fCI7IVTTz_1_5x sx_e1ddd6")
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_form)
            )
            if EC.presence_of_element_located(self.login_form) :
                self.creat_new_acount = self.driver.find_element(*self.creat_new_account)
                self.creat_new_acount.click()
        except: assert False
        


    def test_01_Required_Fields(self):
        """Check the required fields by not filling any data"""
        try:#clicking the sinup button
            main = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sinup_button)
            )
            main.click()
            self.driver.find_element(*self.sinup_button).click()
        except: assert False

        
        try:#checking the mandatory_symbol
            textfileds_mandatorys = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(self.textfiled_mandatory_symbol)
            )
            radios_mandatorys = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(self.radio_mandatory_symbol)
            )
            assert len(textfileds_mandatorys) == 4 & len(radios_mandatorys) == 2
        except: assert False



    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()

if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()
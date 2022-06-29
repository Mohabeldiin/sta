"""Passing invalid email and invalid password
 TC_04_LOGIN 
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 4")

class test_04_login(unittest.TestCase):
    """Passing invalid phone number and invalid password"""
    
    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")
    
    def test_04(self):
        """Passing invalid phone number and invalid password"""
        try:
            self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_NUM)
            self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_NUM)
            self.login.click()  # pylint: disable=no-member
            self.assertTrue(self.email.is_displayed(), "Email field is not displayed")
            self.assertTrue(self.password.is_displayed(), "Password field is not displayed")
        except:
            pass    
    
    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)
   

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuit(test_04_login))
    runner = unittest.TestTestRunner()
    runner.run(suite)                
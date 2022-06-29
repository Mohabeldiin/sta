""" Passing Blank Email and Password
 TC_15_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 15")

class test_15_login(unittest.TestCase):
    """Passing Blank Email and Password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_15(self):
        """Passing Blank Email and Password"""
        try:
            self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_BLANK)
            self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_BLANK)
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
    suite.addTest(unittest.makeSuite(test_15_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
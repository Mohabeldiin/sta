""" Verify that the validation error message should be displayed properly with proper helper text
 TC_16_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 16")

class test_16_login(unittest.TestCase):
    """Verify that the validation error message should be displayed properly with proper helper text"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_16(self):
        """Verify that the validation error message should be displayed properly with proper helper text"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_INVALID)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_VALID)
        self.login.click()  # pylint: disable=no-member
        self.assertTrue(self.email.is_displayed(), "Email field is not displayed")
        self.assertTrue(self.password.is_displayed(), "Password field is not displayed")
        self.assertTrue(self.email_error.is_displayed(), "Email error message is not displayed")
        self.assertTrue(self.password_error.is_displayed(), "Password error message is not displayed")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)     

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_16_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
            
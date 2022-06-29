""" Verify that fb login functionality with an old password.
 TC_18_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 18") 

class test_18_login(unittest.TestCase):
    """Verify that fb login functionality with an old password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_18(self):
        """Verify that fb login functionality with an old password"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_VALID)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.OLD_PASSWORD)
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
    suite.addTest(unittest.makeSuite(test_18_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
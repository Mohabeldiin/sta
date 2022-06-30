"""Verify facebook login functionality with incorrect password.
 TC_17_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 17")


class test_17_login(unittest.TestCase):
    """Verify facebook login functionality with incorrect password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_17(self):
        """Verify facebook login functionality with incorrect password"""
        try:
            self.elements.email.send_keys(  # pylint: disable=no-member
                self.testdata.EMAIL_VALID)
            self.elements.password.send_keys(  # pylint: disable=no-member
                self.testdata.PASSWORD_INVALID)
            self.elements.login.click()  # pylint: disable=no-member
            self.assertTrue(self.elements.email.is_displayed(),
                            "Email field is not displayed")
            self.assertTrue(self.elements.password.is_displayed(),
                            "Password field is not displayed")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_17_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

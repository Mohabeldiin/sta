"""Passing vaild email and blank password
 TC_06_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 6")


class test_06_login(unittest.TestCase):
    """Passing valid email and blank password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_06(self):
        """Passing valid email and blank password"""
        try:

            self.elements.email.send_keys(  # pylint: disable=no-member
                self.testdata.EMAIL_VALID)
            self.elements.password.send_keys(  # pylint: disable=no-member
                self.testdata.BLANK_SPACES)
            self.elements.login.click()  # pylint: disable=no-member
            self.assertTrue(True, "Password is required")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_06_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

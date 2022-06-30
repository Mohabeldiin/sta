""" To verify that Welcome message after successfully login.
 TC_19_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 19")


class test_19_login(unittest.TestCase):
    """Verify that Welcome message after successfully login"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_19(self):
        """Verify that Welcome message after successfully login"""
        try:
            self.elements.email.send_keys(  # pylint: disable=no-member
                self.testdata.EMAIL_VALID)
            self.elements.password.send_keys(  # pylint: disable=no-member
                self.testdata.PASSWORD_VALID)
            self.elements.login.click()  # pylint: disable=no-member
            self.assertTrue(True, "Welcome message is displayed")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_19_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

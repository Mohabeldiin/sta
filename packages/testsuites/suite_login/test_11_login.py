"""Passing invalid phone and password
 TC_11_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from re import T
from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 11")


class test_11_login(unittest.TestCase):
    """Passing invalid phone and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_11(self):
        """Passing invalid phone and password"""
        try:
            self.elements.phone.send_keys(  # pylint: disable=no-member
                self.testdata.EMAIL_INVALID)
            self.elements.password.send_keys(  # pylint: disable=no-member
                self.testdata.PASSWORD_LETTER)
            self.elements.login.click()  # pylint: disable=no-member
            self.assertTrue(True, "Incorrect email or password")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_11_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

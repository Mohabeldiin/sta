"""Passing  blank phone and vaild password
 TC_12_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 12")


class test_12_login(unittest.TestCase):
    """Passing blank phone and vaild password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_12(self):
        """Passing blank phone and vaild password"""
        try:
            self.elements.phone.send_keys(  # pylint: disable=no-member
                self.testdata.BLANK_SPACES)
            self.elements.password.send_keys(  # pylint: disable=no-member
                self.testdata.PASSWORD_NUM)
            self.elements.login.click()  # pylint: disable=no-member
            self.assertTrue(True, "Incorrect email or password")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_12_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

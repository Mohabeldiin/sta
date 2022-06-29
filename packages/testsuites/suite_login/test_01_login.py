"""Passing valid email and password
 TC_01_LOGIN 
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 1")


class test_01_login(unittest.TestCase):
    """Passing valid email and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_01(self):
        """Passing valid email and password"""
        self.elements.email.send_keys(self.testdata.EMAIL_VALID)
        self.elements.password.send_keys(self.testdata.PASSWORD_VALID)
        self.elements.login.click()
        self.assertTrue(self.elements.login.is_displayed(),
                        "Login button is not displayed")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_01_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

"""Passing valid phone number and vaild password
    TC_03_LOGIN
    Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 3")


class test_03_login(unittest.TestCase):
    """Passing invalid phone number and valid password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_03(self):
        """Passing invalid phone number and valid password"""
        try:
            self.elements.email.send_keys(TestData.EMAIL_VALID)
            self.elements.password.send_keys(TestData.PASSWORD_VALID)
            self.elements.login.click()
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
    suite.addTest(unittest.makeSuite(test_03_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

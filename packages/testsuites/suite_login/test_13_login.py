"""Verify of the length email and password
 TC_13_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 13")

class test_13_login(unittest.TestCase):
    """Verify of the length email and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_13(self):
        """Verify of the length email and password"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_NUM)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_NUM)
        self.login.click()  # pylint: disable=no-member
        self.assertTrue(self.classifier.find_text_field_matching_label(# pylint: disable=no-member
            "login").is_displayed(), "Login button is displayed")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_13_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
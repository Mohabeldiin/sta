"""Passing invalid phone and vaild password
 TC_10_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 10")

class test_10_login(unittest.TestCase):  # pylint: disable=invalid-name

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_10(self):
        """Passing invalid phone and vaild password"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_NUM)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_VALID)
        self.login.click()  # pylint: disable=no-member
        incorrect = self.classifier.find_text_field_matching_label(# pylint: disable=no-member
            "incorrect")
        self.assertTrue(incorrect.is_displayed(), "Incorrect email or password")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_10_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
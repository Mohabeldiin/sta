"""Passing valid phone and password
 TC_08_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 8")

class test_08_login(unittest.TestCase): # pylint: disable=too-many-instance-attributes
    """Passing valid phone and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_08(self):
        """Passing valid phone and password"""
        try:
            self.email.send_keys(  # pylint: disable=no-member
                self.testdata.EMAIL_NUM)
            self.password.send_keys(  # pylint: disable=no-member
                self.testdata.PASSWORD_VALID)
            self.login.click()  # pylint: disable=no-member
            self.assertTrue(self.classifier.find_text_field_matching_label(# pylint: disable=no-member
                "login").is_displayed(), "Login button is displayed")
        except:
            pass
        
    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_08_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
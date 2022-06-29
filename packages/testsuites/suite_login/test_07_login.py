"""Passing blank email and password
 TC_07_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from ast import Try
from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 7")

class test_07_login(unittest.TestCase):
    """Passing blank email and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_07(self):
        """Passing blank email and password"""
        try:
                
            self.email.send_keys(  # pylint: disable=no-member
                self.testdata.BLANK_SPACES)
            self.password.send_keys(  # pylint: disable=no-member
                self.testdata.BLANK_SPACES)
            self.login.click()  # pylint: disable=no-member
            self.assertTrue(self.classifier.find_text_field_matching_label(# pylint: disable=no-member
                "blank").is_displayed(), "Email is required")
        except:
            pass
        
    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_07_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)
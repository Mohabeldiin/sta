"""Check the required fields by not filling any data
    TC_02_Registration
    Refer to https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import *  # pylint: disable = unused-wildcard-import, wildcard-import

logger = project_logger("Registration Test Case 1")


class Test_02_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1-Do not enter any value in the field.
        2-Click on the Register button."""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)

    def test_01_Required_Fields(self):  # pylint: disable = invalid-name
        """Check the required fields by not filling any data"""
        self.sinup.click()  # pylint: disable = no-member
        a1 = self.email.get_attribute(  # pylint: disable = no-member
            "value aria-required")  # pylint: disable = no-member
        a2 = self.password.get_attribute(  # pylint: disable = no-member
            "aria-required") == "true"  # pylint: disable = no-member
        self.assertTrue(self.email.get_attribute("aria-required"),  # pylint: disable = no-member
                        "Fields are not Required")
        self.assertTrue(self.password.get_attribute("aria-required") == "true",  # pylint: disable = no-member
                        "Fields are not Required")

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_02_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

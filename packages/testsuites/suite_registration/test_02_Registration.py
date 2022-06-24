"""Check the required fields by not filling any data
    TC_02_Registration
    Refer to https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 2")


class Test_02_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1-Do not enter any value in the field.
        2-Click on the Register button."""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Required_Fields(self):  # pylint: disable = invalid-name
        """Check the required fields by not filling any data"""
        self.sinup.click()  # pylint: disable = no-member
        self.assertTrue(self.elements.email.get_attribute("aria-required"),  # pylint: disable = no-member
                        "Fields are not Required")
        self.assertTrue(self.elements.password.get_attribute("aria-required") == "true",  # pylint: disable = no-member
                        "Fields are not Required")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_02_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

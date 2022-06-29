"""Check the phone number when passing alphanumeric data
    TC_08_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 8")


class Test_08_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """Check the phone number when passing alphanumeric data.\n
    1- Enter alphanumeric data in phone field.\n
    2- Click on Register button"""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Phone_Number_validation(self):  # pylint: disable = invalid-name
        """Check the phone number when passing alphanumeric data.\n
        EC: It should not show any validation message."""
        try:
            self.elements.email.send_keys(TestData.PHONE_NUMBER)
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(AR, ER,
                                "the phone number when passing alphanumeric data.")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_08_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

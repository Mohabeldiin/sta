"""this test case Check the password limit when enter value less than min
    TC_11_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 9")


class Test_11_Registration(unittest.TestCase):
    """Check the password limit when enter value less than min\n
    1- Enter value which is alphanumeric but less than 8.\n
    2- Click on Register button.
    NOTE:
            This is a Not Applicable Test Case.
            facebook does not have validation message for password length."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Password_Validation(self):
        """Check the password limit when enter value less than min\n
        EC: It should show validation message."""
        self.elements.password.send_keys(
            TestData.PASSWORD_LENGTH_LESS_THAN_MIN)
        self.elements.sinup.click()
        ER = True
        AR = bool(self.elements.password.get_attribute(
            'aria-invalid') == "true")
        self.assertNotEqual(
            AR, ER, "the password length when enter value less than min.")

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_11_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

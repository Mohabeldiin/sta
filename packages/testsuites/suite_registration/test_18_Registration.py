"""Phone Number Validation
    TC_18_Registration from
    https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver


logger = project_logger("Registration Test Case 18")


class Test_18_Registration(unittest.TestCase):
    """Verify if the length of the phone number is incorrect"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_registration(self):
        """Verify if the length of the phone number is incorrect i.e. more than 10.
            1- Enter phone number more than 10 digits.
            2- Enter all required fields.
            3- Click on Register Button.
            EC: It should show the validation error message for phone number length."""
        try:
            self.elements.fname.send_keys(TestData.FRIST_NAME)
            self.elements.lname.send_keys(TestData.LAST_NAME)
            self.elements.email.send_keys(
                TestData.PHONE_NUMBER_LENGTH_MORE_THAN_MIN)
            self.elements.password.send_keys(TestData.PASSWORD_NUM_LETTER)
            self.elements.day.click()
            self.elements.month.click()
            self.elements.year.click()
            self.elements.gender.click()
            self.elements.sinup.click()
        except:
            pass
        finally:
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(
                AR, ER, "Length of the phone number is incorrect.")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_18_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

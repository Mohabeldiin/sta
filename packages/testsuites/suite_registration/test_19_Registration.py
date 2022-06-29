"""Password Validation
    TC_19_Registration from
    https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver


logger = project_logger("Registration Test Case 19")


class Test_19_Registration(unittest.TestCase):
    """Verify if the password required rules are not satisfied in the password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_registration(self):
        """Verify if the password required rules are not satisfied in the password
            1- Enter the password which not satisfies the required rule.
            2- Click on Register button.
            EC:It should display error with required rules for password value
            (like it should contain a special character, a small case, a number)"""
        try:
            self.elements.fname.send_keys(TestData.FRIST_NAME)
            self.elements.lname.send_keys(TestData.LAST_NAME)
            self.elements.email.send_keys(TestData.EMAIL_INVALID)
            self.elements.password.send_keys(TestData.PASSWORD_LETTER)
            self.elements.day.click()
            self.elements.month.click()
            self.elements.year.click()
            self.elements.gender.click()
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.password.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(
                AR, ER, "Length of the phone number is incorrect.")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_19_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

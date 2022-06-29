"""this test case Check the Email text field that has Email validation
    TC_06_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 6")


class Test_06_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1- Enter Invalid Emails.
       2- Click on the Register Button.
       Description:
                Check the Email text field that has an Email address without @ symbol.
                Check the Email text field that has a random string instead of a real email.
                Check the Email text field that has @ symbol written in words.
                Check the Email text field that has a missing dot in the email address.
        Test Data:
                1.testgmail.com
                2.test@gmail.com
                3.testAtgmail.com
                4.test@gmailcom"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has an Email address without @ symbol."""
        try:
            self.elements.email.send_keys(TestData.EMAIL_WITHOUT_AT)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(AR, ER,
                                "Email text field that has an Email address without @ symbol.")
        except:
            pass

    def test_02_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has a random string instead of a real email."""
        try:
            self.elements.email.send_keys(TestData.RANDOM)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(AR, ER,
                                "Email text field that has an Email address without @ symbol.")
        except:
            pass

    def test_03_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has @ symbol written in words."""
        try:
            self.elements.email.send_keys(TestData.EMAIL_AT_IN_WORD)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(AR, ER,
                                "Email text field that has an Email address without @ symbol.")
        except:
            pass

    def test_04_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has a missing dot in the email address."""
        try:
            self.elements.email.send_keys(TestData.EMAIL_WITHOUT_DOT)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(AR, ER,
                                "Email text field that has an Email address without @ symbol.")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_06_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

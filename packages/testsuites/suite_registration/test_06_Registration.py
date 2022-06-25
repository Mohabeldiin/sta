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
        self.elements.email.send_keys(TestData.EMAIL_WITHOUT_AT)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has an Email address without @ symbol.")

    def test_02_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has a random string instead of a real email."""
        self.elements.email.send_keys(TestData.RANDOM)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has a random string instead of a real email.")

    def test_03_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has @ symbol written in words."""
        self.elements.email.send_keys(TestData.EMAIL_AT_IN_WORD)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has @ symbol written in words.")

    def test_04_Email_validation(self):  # pylint: disable = invalid-name
        """Check the Email text field that has a missing dot in the email address."""
        self.elements.email.send_keys(TestData.EMAIL_WITHOUT_DOT)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has a missing dot in the email address.")

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_06_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

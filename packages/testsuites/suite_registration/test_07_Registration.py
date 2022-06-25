"""Check all the valid emails
    TC_07_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 7")


class Test_07_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """Check all the valid emails.
    1- Enter valid Emails.
    2- Click on the Register Button."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Email_validation(self):  # pylint: disable = invalid-name
        """Check the valid email: test.22@gmail.com.
        EC: It should not show any validation message."""
        self.elements.email.send_keys(TestData.EMAIL_INVALID2)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has @ symbol written in words.")

    def test_02_Email_validation(self):  # pylint: disable = invalid-name
        """Check the valid email: test@gmail.com.
        EC: It should not show any validation message."""
        self.elements.email.send_keys(TestData.EMAIL_INVALID)
        # ree email
        self.elements.sinup.click()
        #self.assertTrue(foo ,"Email text field that has @ symbol written in words.")

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_07_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

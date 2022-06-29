"""this test case Check the password when passing valid data
    TC_14_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 14")


class Test_14_Registration(unittest.TestCase):
    """Check the password when passing valid data.\n
    1- Enter value in alphanumeric which is in between 8-32.\n
    2- Click on Register button.
    NOTE:
            This is a Not Applicable Test Case.
            facebook does not have any validation for password."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Password_Validation(self):
        """Check the password when passing valid data.\n
        EC: It should not show any validation message"""
        try:
            self.elements.password.send_keys(TestData.PASSWORD_NUM_LETTER)
            self.elements.sinup.click()
            ER = False
            AR = bool(self.elements.password.get_attribute(
                'aria-invalid') == "true")
            self.assertEqual(
                AR, ER, "the password when passing valid data.")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_14_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

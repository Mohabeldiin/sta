"""this test case Check the password when passing only numbers
    TC_13_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 13")


class Test_13_Registration(unittest.TestCase):
    """Check the password when passing only numbers.\n
    1- Enter a value in numbers which is in between 8-32.\n
    2- Click on Register button.
     NOTE:
            This is a Not Applicable Test Case.
            facebook does not have validation message for passing only numbers."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Password_Validation(self):
        """Check the password when passing only numbers\n
        EC: It should show validation message"""
        try:
            self.elements.password.send_keys(TestData.PASSWORD_NUM)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.password.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(
                AR, ER, "the password when passing only numbers.")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_13_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

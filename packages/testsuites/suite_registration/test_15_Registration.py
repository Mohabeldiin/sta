"""this test case Verify if blank spaces are passed in required fields.
    TC_15_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 15")


class Test_15_Registration(unittest.TestCase):
    """Verify if blank spaces are passed in required fields.\n
    1- Go to the Site.\n
    2- Passed blank spaces in required fields.\n
    3- Click on the Register button.\n"""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Required_Fields(self):
        """Verify if blank spaces are passed in required fields.\n
        EC: Those Blank spaces should trim and Validation error message for required fields should visible.\n"""
        self.elements.fname.send_keys(TestData.BLANK_SPACES)
        self.elements.lname.send_keys(TestData.BLANK_SPACES)
        self.elements.email.send_keys(TestData.BLANK_SPACES)
        self.elements.password.send_keys(TestData.BLANK_SPACES)
        self.elements.sinup.click()
        ER = True
        AR = bool(self.elements.fname.get_attribute(
            'aria-invalid') == "true")
        self.assertEqual(
            AR, ER, "the blank spaces in required fields.")

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_15_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

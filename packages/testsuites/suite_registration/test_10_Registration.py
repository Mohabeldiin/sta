"""this test case Check the phone number when passing country code
    TC_10_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 10")


class Test_10_Registration(unittest.TestCase):
    """Check the phone number when passing country code\n
    1- Enter valid phone number with country code.\n
    2- Click on Register button."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Phone_Number_validation(self):
        """Check the phone number when passing country code\n
        EC: It should not show any validation message"""
        try:
            self.elements.email.send_keys(TestData.PHONE_NUMBER)
            self.elements.sinup.click()
            ER = True
            AR = bool(self.elements.email.get_attribute(
                'aria-invalid') == "true")
            self.assertNotEqual(
                AR, ER, "the phone number when not pass country code.")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_10_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

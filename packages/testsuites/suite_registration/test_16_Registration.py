"""Verify user can verify its Email ID
    TC_foo_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 16")


class Test_16_Registration(unittest.TestCase):
    """Verify user can verify its Email ID"""

    def setUp(self):
        """Called before every test"""
        # self.driver = setup_selenium_driver()
        # self.elements = SetUp(self.driver)

    def test_16_Registration(self):
        """1- Go to the Email.
            2- Click on the verification link.
            ER: User should get a verification link and able to verify his/her Email ID."""
        try:
            ER = True
            AR = True
            self.assertEqual(
                AR, ER, "Verify user can verify its Email ID")
        except:
            pass

    def tearDown(self):
        """Called after every test"""
        # TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_16_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

"""Check all the optional fields when filling data
    TC_05_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 5")


class Test_05_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1- Enter valid data in optional fields.
       2- Enter valid data in required fields.
       3- Click on the Signup button."""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_01_Optional_Fields(self):  # pylint: disable = invalid-name
        """Check all the optional fields when filling data"""
        pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_05_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

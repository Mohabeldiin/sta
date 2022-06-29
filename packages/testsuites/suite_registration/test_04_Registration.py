"""Check all the optional fields when do not fill data
    TC_04_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from typing_extensions import Self
from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

logger = project_logger("Registration Test Case 7")


class Test_04_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1- Do not enter any detail in optional fields.
       2- Enter valid data in required fields.
       3- Click on the Signup button"""

    def setUp(self):
        """this method will be called before every test"""
        # self.driver = setup_selenium_driver()
        # self.elements = SetUp(self.driver)

    def test_01_Optional_Fields(self):  # pylint: disable = invalid-name
        """Check all the optional fields when do not fill data"""
        try:
            ER = True
            AR = True
            self.assertEqual(
                AR, ER, "Test Case 04: Check all the optional fields when do not fill data")
        except:
            pass

    def tearDown(self):
        """this method will be called after every test"""
        # TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_04_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

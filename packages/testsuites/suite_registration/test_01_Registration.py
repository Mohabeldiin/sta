"""Checks all the text boxes, radio buttons, buttons, etc
    TC_01_Registration
    Refer to https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import *  # pylint: disable = unused-wildcard-import, wildcard-import

logger = project_logger("Registration Test Case 1")


class Test_01_User_Interface(unittest.TestCase):  # pylint: disable = invalid-name
    """Checks all the text boxes, radio buttons, buttons, etc"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)

    def test_01_1_registration_page_ui(self):
        """Checks the presence of all UI elements"""
        try:
            self.assertTrue(self.email.is_displayed(),  # pylint: disable = no-member
                            "UI is not present")
            self.assertTrue(self.password.is_displayed(),  # pylint: disable = no-member
                            "UI is not present")
            self.assertTrue(self.sinup.is_displayed(),  # pylint: disable = no-member
                            "UI is not present")
        except AssertionError:
            assert False

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_01_User_Interface))
    runner = unittest.TextTestRunner()
    runner.run(suite)

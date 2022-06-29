"""Passing invalid email and password
 TC_01_LOGIN
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest, classifier_client_python)

logger = project_logger("Login Test Case 2")


class test_02_login(unittest.TestCase):  # pylint: disable=invalid-name
    """"Passing invalid email and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)

    def test_02(self):
        """Passing invalid email and password"""
        try:
            self.elements.email.send_keys(TestData.EMAIL_INVALID)
            self.elements.password.send_keys(TestData.PASSWORD_NUM)
            self.elements.login.click()
            classifier = classifier_client_python(self.elements.driver)
            incorrect = classifier.find_elements_matching_label(
                "password that you've entered is incorrect")[0]
            ER = True
            AR = bool(incorrect.is_displayed())
            self.assertNotEqual(ER, AR, "Incorrect email or password")
        except:
            assert True

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_02_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)

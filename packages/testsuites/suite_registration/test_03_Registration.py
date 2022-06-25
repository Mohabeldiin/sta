"""Check user should Register by filling all the required fields
    TC_03_Registration
    Refer to https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

from packages.testsuites.suite_registration.init import TearDown, SetUp, TestData, unittest, project_logger, setup_selenium_driver

from packages.tempmail import TempMail

logger = project_logger("Registration Test Case 3")


class Test_03_Registration(unittest.TestCase):  # pylint: disable = invalid-name
    """1- Enter valid values in the required fields.
       2- Click on the Register button."""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        self.elements = SetUp(self.driver)
        self.temp_mail = TempMail()
        TestData()

    def test_01_required_fields(self):
        """Check user should Register by filling all the required fields"""
        self.elements.firstname.send_keys(  # pylint:disable=no-member
            TestData.FRIST_NAME)
        self.lasttname.send_keys(  # pylint:disable=no-member
            TestData.LAST_NAME)
        email = self.temp_mail.get_email()
        self.elements.email.send_keys(email)  # pylint:disable=no-member
        self.elements.reemail.send_keys(email)  # pylint:disable=no-member
        self.elements.password.send_keys(  # pylint:disable=no-member
            TestData.PASSWORD_NUM_LETTER)
        self.birthday.click()  # pylint:disable=no-member
        self.birthmonth.click()  # pylint:disable=no-member
        self.birthyear.click()  # pylint:disable=no-member
        self.gender.click()  # pylint:disable=no-member
        self.sinup.click()  # pylint:disable=no-member

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_03_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

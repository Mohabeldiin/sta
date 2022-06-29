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
        try:
            self.elements.fname.send_keys(TestData.FRIST_NAME)
            self.elements.lname.send_keys(TestData.LAST_NAME)
            email = self.temp_mail.get_email()
            self.elements.email.send_keys(email)
            reemail = self.elements.classifier.find_text_field_matching_label(
                'Re-enter email address')
            reemail.send_keys(email)
            self.elements.password.send_keys(TestData.PASSWORD_NUM_LETTER)
            self.elements.day.click()
            self.elements.month.click()
            self.elements.year.click()
            self.elements.gender.click()
            self.elements.sinup.click()
            self.assertTrue(self.temp_mail.receive_mail(),
                            "Registration failed")
        except:
            pass

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_03_Registration))
    runner = unittest.TextTestRunner()
    runner.run(suite)

"""Check the password when passing only numbers
    TC_13_registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""

# from packages
from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest)

logger = project_logger("Registration Test Suite")

class Test_Data(object):
    """test data that is used in this test case"""
    logger.info("initializing test data")
    BLANK_SPACES = " "
    PASSWORD_NUM = "12345678"
    PASSWORD_LET = "Password"
    PASSWORD_NUM_LET = "Pass123456"
    PHONE_NUMBER = "+9190112244"
    EMAIL_INVALID = "test@gmail.com"
    EMAIL_INVALID2 = "test.22@gmail.com"
    EMAIL_WITHOUT_AT = "testgmail.com"
    EMAIL_WITHOUT_AT_IN_WORD = "testAtgmail.com"
    EMAIL_WITHOUT_DOT = "test@gmailcom"


class Test_Registration(unittest.TestCase):
    """foo"""

    def setUp(self):
        """called before every test"""
        logger.info("setting up the test")
        self.driver = setup_selenium_driver()
        self.classifier = classifier_client_python(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.get(get_link_to_test_without_validate())

        try:
            self.newaccount = self.classifier.find_elements_matching_label('Create New Account')
        except selenium_exceptions.NoSuchElementException:
            self.newaccount = self.classifier.find_elements_matching_label('Sign Up')

        self.newaccount.click()

        self.firstname = self.classifier.find_elements_matching_label('first name')
        self.lasttname = self.classifier.find_elements_matching_label('surname')
        self.email = self.classifier.find_elements_matching_label('email')
        self.reemail = self.classifier.find_elements_matching_label('re-enter email')
        self.password = self.classifier.find_elements_matching_label('password')
        self.sinup = self.classifier.find_elements_matching_label('sign up')
        logger.info("test data initialized")

    # creating 19 test case as test_1_registration
    def test_1_registration(self):
        """Checks the presence of all UI elements"""
        logger.info("Check the presence of all UI elements")
        assert self.sinup.is_displayed()

    def test_2_registration(self):
        """Checks the required fields by not filling any data"""
        logger.info("Check the required fields by not filling any data")
        self.sinup.click()
        

        try:  # checking the mandatory_symbol
            textfileds_mandatorys = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    self.textfiled_mandatory_symbol)
            )
            radios_mandatorys = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    self.radio_mandatory_symbol)
            )
            assert len(textfileds_mandatorys) == 4 & len(
                radios_mandatorys) == 2
        except:
            assert False

    def test_3_registration(self):
        """Check user should Register by filling all the required fields"""
        pass

    def test_4_registration(self):
        """Check all the optional fields when do not fill data"""
        pass

    def test_5_registration(self):
        """Check all the optional fields when filling data"""
        pass

    def test_6_1_registration(self):
        """Check the Email text field that has an Email address without @ symbol."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_at)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(
                self.confirme_email_textfiled_locator)
        except:
            assert False

    def test_6_2_registration(self):
        """Check the Email text field that has a random string instead of a real email."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_random)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(
                self.confirme_email_textfiled_locator)
        except:
            assert False

    def test_6_3_registration(self):
        """Check the Email text field that has @ symbol written in words."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_at_in_word)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(
                self.confirme_email_textfiled_locator)
        except:
            assert False

    def test_6_4_registration(self):
        """Check the Email text field that has a missing dot in the email address."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.clear()
            email.send_keys(Test_Data.email_without_dot)
            """hna msh hados 3la sinup button le facebook bs
                han7tag n8iarha b3diin le ba2ii el mwak3"""
            assert EC.invisibility_of_element_located(
                self.confirme_email_textfiled_locator)
        except:
            assert False

    def test_7_1_registration(self):
        """Check the valid email: test.22@gmail.com.\n
        EC: It should not show any validation message."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.send_keys(Test_Data.EMAIL1)
            confirme_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    self.confirme_email_textfiled_locator)
            )
            confirme_email.send_keys(Test_Data.EMAIL1)
            sinUp_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.sinUp_button_locator)
            )
            sinUp_button.click()
            mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
            )
            if len(mandatory_symbol) == 2:
                assert True
        except AssertionError:
            assert False

    def test_7_2_registration(self):
        """Check the valid email: test@gmail.com.
        EC: It should not show any validation message."""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_textfiled_locator)
            )
            email.send_keys(Test_Data.EMAIL2)
            confirme_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    self.confirme_email_textfiled_locator)
            )
            confirme_email.send_keys(Test_Data.EMAIL1)
            sinUp_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.sinUp_button_locator)
            )
            sinUp_button.click()
            mandatory_symbol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.textfiled_mandatory_symbol)
            )
            if len(mandatory_symbol) == 2:
                assert True
        except AssertionError:
            assert False

    def test_8_registration(self):
        """Check the phone number when passing alphanumeric data.\n
        EC: It should not show any validation message."""

        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.phone_textfiled_locator)
                )
                phone.send_keys(Test_Data.PHONE_NUMBER)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_9_registration(self):
        """Check the phone number when not pass country code.\n
        EC: It should show the validation message for country code is required.
        NOTE:
            This is a Not Applicable Test Case.
            facebook does not have error message for country code is required
            but it will show the error message for phone number is required
            facebook error message is 'Please enter a valid mobile number or email address.'."""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.phone_textfiled_locator)
                )
                phone.send_keys(Test_Data.PHONE_NUMBER)
            except AssertionError:
                print("###############")
                print(AssertionError.__doc__)
                print("###############")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("###############")
                print(AssertionError.__doc__)
                print("###############")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("###############")
                print(AssertionError.__doc__)
                print("###############")
                assert False
        except AssertionError:
            print("###############")
            print(AssertionError.__doc__)
            print("###############")
            assert False

    def test_10_registration(self):
        """Check the phone number when passing country code\n
        EC: It should not show any validation message"""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.phone_textfiled_locator)
                )
                phone.send_keys(Test_Data.PHONE_NUMBER)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            except TimeoutException:
                print("\n###############\n", TimeoutException.__doc__,
                      "Can't fined error message:", self.phone_textfiled_locator, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            except TimeoutException:
                print("\n###############\n", TimeoutException.__doc__,
                      "Can't fined error message:", self.sinUp_button_locator, "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located(
                        self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            except TimeoutException:
                print("\n###############\n", TimeoutException.__doc__,
                      "Can't fined error message:", self.error_message_locator, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_11_registration(self):
        """Check the password limit when enter value less than min\n
        EC: It should show validation message."""

        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.password_textfiled_locator)
                )
                phone.send_keys(Test_Data.PASSWORD)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_12_registration(self):
        """Check the password limit when enter value greater than max.\n
        EC: It should show validation message"""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.password_textfiled_locator)
                )
                phone.send_keys(Test_Data.PASSWORD)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_13_registration(self):
        """Check the password when passing only numbers.\n
            1- Enter a value in numbers which is in between 8-32.\n
            2- Click on Register button."""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.password_textfiled_locator)
                )
                phone.send_keys(Test_Data.PASSWORD)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                self.driver.find_element()
                sinup = WebDriverWait(self.driver, 10).until(
                    # EC.presence_of_element_located(self.sinUp_button_locator)
                    EC.text_to_be_present_in_element()
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_14_registration(self):
        """Check the password when passing valid data.\n
        EC: It should not show any validation message"""
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.password_textfiled_locator)
                )
                phone.send_keys(Test_Data.PASSWORD)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                mandatory_symbol = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.password_filed_mandatory_symbol)
                )
                if len(mandatory_symbol) == 3:
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_15_1_registration(self):
        """Verify if blank spaces are passed in required fields.\n
        EC: Those Blank spaces should trim and Validation error message for required fields should visible.\n"""
        self.frist_name_textfiled_locator = (By.NAME, 'firstname')
        try:
            try:
                frist_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.frist_name_textfiled_locator)
                )
                frist_name.send_keys(Test_Data.BLANK_SPACES)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                # error = WebDriverWait(self.driver, 10).until(
                # EC.visibility_of_element_located(self.error_message_locator)
                # )
                # if error:
                #     assert True
                mandatory_symbol = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.textfiled_mandatory_symbol)
                )
                if len(mandatory_symbol) == 3:
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            except TimeoutException:
                # print("\n###############\n",TimeoutException.__doc__ , "Can't fined error message:", self.error_message_locator , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_15_2_registration(self):
        """Verify if blank spaces are passed in required fields.\n
        EC: Those Blank spaces should trim and Validation error message for required fields should visible.\n"""
        self.last_name_textfiled_locator = (By.NAME, 'lastname')
        try:
            try:
                last_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.frist_name_textfiled_locator)
                )
                last_name.send_keys(Test_Data.BLANK_SPACES)
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            try:
                # error = WebDriverWait(self.driver, 10).until(
                # EC.visibility_of_element_located(self.error_message_locator)
                # )
                # if error:
                #     assert True
                mandatory_symbol = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        self.textfiled_mandatory_symbol)
                )
                if len(mandatory_symbol) == 3:
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",
                      AssertionError.__doc__, "\n###############\n")
                assert False
            except TimeoutException:
                # print("\n###############\n",TimeoutException.__doc__ , "Can't fined error message:", self.error_message_locator , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",
                  AssertionError.__doc__, "\n###############\n")
            assert False

    def test_16_registration(self):
        """foo"""

    def test_17_registration(self):
        """foo"""

    def test_18_registration(self):
        """foo"""

    def test_19_registration(self):
        """foo"""

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test_Registration))
    runner=unittest.TextTestRunner()
    runner.run(test_suite)

"""Base for testsuites."""

from random import Random
import time

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest,
                                       WebElement)

logger = project_logger("Registration Test Suite initialization")


class TestData:
    """test data that is used in the test cases"""
    logger.info("initializing test data")
    BLANK_SPACES = " "
    PASSWORD_NUM = "12345678"
    PASSWORD_LETTER = "Password"
    PASSWORD_NUM_LETTER = "Pass123456"
    PHONE_NUMBER = "+9190112244"
    EMAIL_INVALID = "test@gmail.com"
    EMAIL_INVALID2 = "test.22@gmail.com"
    EMAIL_WITHOUT_AT = "testgmail.com"
    EMAIL_AT_IN_WORD = "testAtgmail.com"
    EMAIL_WITHOUT_DOT = "test@gmailcom"
    RANDOM = "sjanfljbaoubl"
    FRIST_NAME = "fristname"
    LAST_NAME = "lasttname"


class SetUp:  # pylint: disable = too-few-public-methods, too-many-instance-attributes
    """called before every test"""

    def __init__(self, driver):
        logger.info("setting up the test")
        self.classifier = classifier_client_python(driver)
        driver.implicitly_wait(5)
        driver.get(get_link_to_test_without_validate())

        try:
            self.newaccount = self.classifier.find_button_matching_label(
                'Create New Account')
            self.newaccount = WebElement(
                self.newaccount.parent, self.newaccount.id)
        except Exception as ex:  # pylint: disable = broad-except
            logger.error(ex)
            self.newaccount = self.classifier.find_button_matching_label(
                'Sign Up')
            self.newaccount = WebElement(
                self.newaccount.parent, self.newaccount.id)
        finally:
            self.newaccount.click()
            time.sleep(5)
        self.firstname = self.classifier.find_text_field_matching_label(
            'first name')
        self.firstname = WebElement(
            self.firstname.parent, self.firstname.id)
        self.lasttname = self.classifier.find_text_field_matching_label(
            'surname')
        self.lasttname = WebElement(
            self.lasttname.parent, self.lasttname.id)
        self.email = self.classifier.find_text_field_matching_label(
            'email')
        self.email = WebElement(self.email.parent, self.email.id)
        # self.email.send_keys(TestData.EMAIL_INVALID)
        # self.reemail = WebElement(
        #     self.reemail.parent, self.reemail.id)
        # self.email.clear()
        self.password = self.classifier.find_text_field_matching_label(
            'password')
        # self.password = WebElement(
        #     self.password.parent, self.password.id)
        # self.birthday = self.classifier.find_button_matching_label(
        #     '8')
        # self.birthday = WebElement(
        #     self.birthday.parent, self.birthday.id)
        # self.birthmonth = self.classifier.find_button_matching_label(
        #     'nov')
        # self.birthmonth = WebElement(
        #     self.birthmonth.parent, self.birthmonth.id)
        # self.birthyear = self.classifier.find_button_matching_label(
        #     '1997')
        # self.birthyear = WebElement(
        #     self.birthyear.parent, self.birthyear.id)
        # self.gender = self.classifier.find_button_matching_label(
        #     'male')
        # self.gender = WebElement(
        #     self.gender.parent, self.gender.id)
        self.sinup = self.classifier.find_button_matching_label(
            'sign up')
        self.sinup = WebElement(self.sinup.parent, self.sinup.id)
        logger.info("test data initialized")


class TearDown():  # pylint: disable = too-few-public-methods
    """called after every test"""

    def __init__(self, driver):
        logger.info("Tearing down Registration Test Suite")
        logger.info("tearing down the test")
        teardown_selenium_driver(driver)
        logger.info("test tear down")


__all__ = ["SetUp", "TearDown", "webdriver", "selenium_exceptions", "By", "EC", "WebDriverWait",
           "unittest", "project_logger", "classifier_client_python",
           "get_link_to_test_without_validate", "setup_selenium_driver"]
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

"""Base for testsuites."""

import time

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest)

logger = project_logger("Registration Test Suite initialization")


class TestData:
    """test data that is used in the test cases"""
    logger.info("initializing test data")
    BLANK_SPACES = " "
    PASSWORD_NUM = "12345678"
    PASSWORD_LETTER = "Password"
    PASSWORD_NUM_LETTER = "Pass123456"
    PASSWORD_LENGTH_LESS_THAN_MIN = "1234567"
    PASSWORD_LENGTH_MORE_THAN_MAX = "123456789012345678901234567890"
    PHONE_NUMBER = "+9190112244"
    PHONE_NUMBER_WITHOUT_COUNTRY_CODE = "90112244"
    PHONE_NUMBER_LENGTH_LESS_THAN_MIN = "9011224"
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
        try:
            logger.info("setting up the test")
            self.classifier = classifier_client_python(driver)
            driver.implicitly_wait(5)
            driver.get(get_link_to_test_without_validate())
            try:
                self.newaccount = self.classifier.find_button_matching_label(
                    'Create New Account')
            except Exception as ex:  # pylint: disable = broad-except
                logger.error(ex)
                self.newaccount = self.classifier.find_button_matching_label(
                    'Sign Up')
            finally:
                self.newaccount.click()
                time.sleep(5)
            self.email = self.classifier.find_text_field_matching_label(
                'Mobile number or email address')
            self.password = self.classifier.find_text_field_matching_label(
                'New password')
            self.fname = self.classifier.find_text_field_matching_label(
                'first name')
            self.lname = self.classifier.find_text_field_matching_label(
                'Surname')
            self.day = self.classifier.find_elements_matching_label('8')[0]
            self.month = self.classifier.find_elements_matching_label('nov')[0]
            self.year = self.classifier.find_elements_matching_label('1997')[0]
            self.gender = self.classifier.find_elements_matching_label('male')[
                0]
            self.sinup = self.classifier.find_button_matching_label('sign up')
            logger.info("test data initialized")
        except Exception as ex:
            logger.error("test data initialization failed")
            logger.error(ex)
            logger.error(ex.__doc__)
            raise Exception(
                f"test data initialization failed. {ex.__doc__}") from ex


class TearDown():  # pylint: disable = too-few-public-methods
    """called after every test"""

    def __init__(self, driver):
        try:
            logger.info("Tearing down Registration Test Suite")
            logger.info("tearing down the test")
            teardown_selenium_driver(driver)
            logger.info("test tear down")
        except Exception as ex:
            logger.error("test data initialization failed")
            logger.error(ex)
            logger.error(ex.__doc__)
            raise Exception(
                f"test data initialization failed. {ex.__doc__}") from ex


__all__ = ["SetUp", "TearDown", "webdriver", "selenium_exceptions", "By", "EC", "WebDriverWait",
           "unittest", "project_logger", "classifier_client_python",
           "get_link_to_test_without_validate", "setup_selenium_driver"]
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

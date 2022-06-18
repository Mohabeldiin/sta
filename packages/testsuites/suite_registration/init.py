"""foo"""

import time

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest,
                                       WebElement)

logger = project_logger("Registration Test Suite initialization")


class TestData(object):
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
    EMAIL_WITHOUT_AT_IN_WORD = "testAtgmail.com"
    EMAIL_WITHOUT_DOT = "test@gmailcom"
    FRIST_NAME = "fristname"
    LAST_NAME = "lasttname"


class SetUp:  # pylint: disable = too-few-public-methods, too-many-instance-attributes
    """called before every test"""

    def __init__(self, testself, driver):
        logger.info("setting up the test")
        testself.classifier = classifier_client_python(driver)
        driver.implicitly_wait(5)
        driver.get(get_link_to_test_without_validate())

        try:
            testself.newaccount = testself.classifier.find_button_matching_label(
                'Create New Account')
            testself.newaccount = WebElement(
                testself.newaccount.parent, testself.newaccount.id)
        except Exception as ex:  # pylint: disable = broad-except
            logger.error(ex)
            testself.newaccount = testself.classifier.find_button_matching_label(
                'Sign Up')
            testself.newaccount = WebElement(
                testself.newaccount.parent, testself.newaccount.id)
        finally:
            testself.newaccount.click()
            time.sleep(5)
        testself.firstname = testself.classifier.find_text_field_matching_label(
            'first name')
        testself.firstname = WebElement(
            testself.firstname.parent, testself.firstname.id)
        testself.lasttname = testself.classifier.find_text_field_matching_label(
            'surname')
        testself.lasttname = WebElement(
            testself.lasttname.parent, testself.lasttname.id)
        testself.email = testself.classifier.find_text_field_matching_label(
            'email')
        testself.email = WebElement(testself.email.parent, testself.email.id)
        testself.reemail = WebElement(
            testself.reemail.parent, testself.reemail.id)
        testself.password = testself.classifier.find_text_field_matching_label(
            'password')
        testself.password = WebElement(
            testself.password.parent, testself.password.id)
        testself.birthday = testself.classifier.find_button_matching_label(
            '8')
        testself.birthday = WebElement(
            testself.birthday.parent, testself.birthday.id)
        testself.birthmonth = testself.classifier.find_button_matching_label(
            'nov')
        testself.birthmonth = WebElement(
            testself.birthmonth.parent, testself.birthmonth.id)
        testself.birthyear = testself.classifier.find_button_matching_label(
            '1997')
        testself.birthyear = WebElement(
            testself.birthyear.parent, testself.birthyear.id)
        testself.gender = testself.classifier.find_button_matching_label(
            'male')
        testself.gender = WebElement(
            testself.gender.parent, testself.gender.id)
        testself.sinup = testself.classifier.find_button_matching_label(
            'sign up')
        testself.sinup = WebElement(testself.sinup.parent, testself.sinup.id)
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

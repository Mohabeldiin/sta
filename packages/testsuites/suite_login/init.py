"""Base for testsuites."""

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest,
                                       WebElement)

logger = project_logger("Login Test Suite initialization")


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
        testself.email = testself.classifier.find_text_field_matching_label(
            'email')
        testself.email = WebElement(
            testself.email.parent, testself.email.id)
        testself.password = testself.classifier.find_text_field_matching_label(
            'password')
        testself.password = WebElement(
            testself.password.parent, testself.password.id)
        testself.login = testself.classifier.find_button_matching_label(
            'Login')
        testself.login = WebElement(
            testself.login.parent, testself.login.id)


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

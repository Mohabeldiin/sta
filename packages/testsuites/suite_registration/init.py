"""foo"""

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest)

logger = project_logger("Registration Test Suite initialization")


class SetUp:  # pylint: disable = too-few-public-methods, too-many-instance-attributes
    """called before every test"""

    def __init__(self, testself, driver):
        logger.info("setting up the test")
        testself.classifier = classifier_client_python(driver)
        driver.implicitly_wait(5)
        driver.get(get_link_to_test_without_validate())

        try:
            testself.newaccount = testself.classifier.find_elements_matching_label(
                'Create New Account')
        except Exception as ex: # pylint: disable = broad-except
            logger.error(ex)
            testself.newaccount = testself.classifier.find_elements_matching_label(
                'Sign Up')
        finally:
            testself.newaccount.click()

        testself.firstname = testself.classifier.find_elements_matching_label(
            'first name')
        testself.lasttname = testself.classifier.find_elements_matching_label(
            'surname')
        testself.email = testself.classifier.find_elements_matching_label(
            'email')
        #testself.reemail = testself.classifier.find_elements_matching_label(
        #    're-enter email')
        testself.password = testself.classifier.find_elements_matching_label(
            'password')
        testself.sinup = testself.classifier.find_elements_matching_label(
            'sign up')
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

"""foo"""

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest)

logger = project_logger("Registration Test Suite initialization")


class SetUp():
    """called before every test"""

    def __init__(self):
        logger.info("Setting up Registration Test Suite")
        logger.info("setting up the test")
        self.driver = setup_selenium_driver()
        self.classifier = classifier_client_python(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.get(get_link_to_test_without_validate())

        try:
            self.newaccount = self.classifier.find_elements_matching_label(
                'Create New Account')
        except selenium_exceptions.NoSuchElementException:
            self.newaccount = self.classifier.find_elements_matching_label(
                'Sign Up')
        finally:
            self.newaccount.click()

        self.firstname = self.classifier.find_elements_matching_label(
            'first name')
        self.lasttname = self.classifier.find_elements_matching_label(
            'surname')
        self.email = self.classifier.find_elements_matching_label('email')
        self.reemail = self.classifier.find_elements_matching_label(
            're-enter email')
        self.password = self.classifier.find_elements_matching_label(
            'password')
        self.sinup = self.classifier.find_elements_matching_label('sign up')
        logger.info("test data initialized")


class TearDown():
    """called after every test"""

    def __init__(self, driver):
        logger.info("Tearing down Registration Test Suite")
        logger.info("tearing down the test")
        teardown_selenium_driver(driver)
        logger.info("test tear down")


__all__ = ["SetUp", "TearDown", "webdriver", "selenium_exceptions", "By", "EC", "WebDriverWait", "unittest",
           "project_logger", "classifier_client_python", "get_link_to_test_without_validate"]
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

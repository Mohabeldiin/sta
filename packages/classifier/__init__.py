"""Classifier for the web elements.

    based on https://github.com/testdotai/classifier-client-python"""

from packages.logger import project_logger

logger = project_logger("Classifier Client")
try:
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logger.error("Selenium is not installed")
    raise ImportError("Please install selenium module") from ImportError

QUERY = "//body//*[not(self::script) and not(self::style) and not(child::*)]"


class ClassifierClient(object):
    """Classifier for the web elements."""

    def __init__(self, driver):
        """initilize the classifier client"""
        logger.info("Initializing Classifier Client")
        self.driver = driver
        # super().__init__()

    def find_elements_matching_label(self, label):
        """finds all page elements matching the label"""
        logger.info("Finding Elements Matching Label: %s", label)
        all_page_elements = self.driver.find_elements_by_xpath(QUERY)
        logger.debug("Page elements found: %s element", len(all_page_elements))
        elements_found = []
        for element in all_page_elements:
            name = element.accessible_name.lower()
            if label in name:
                logger.debug("Found element: %s", name)
                elements_found.append(element)
            else:
                txt = element.text.lower()
                if label in txt:
                    logger.debug("Found element: %s", txt)
                    elements_found.append(element)
        logger.info("Found %s elements", len(elements_found))
        return [WebElement(element.parent,
                           element.id) for element in elements_found]


__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

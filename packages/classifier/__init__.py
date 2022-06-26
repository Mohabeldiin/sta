"""Classifier for the web elements.

    based on https://github.com/testdotai/classifier-client-python"""

from packages.logger import project_logger
from packages.project_selenium import WebElement

logger = project_logger("Classifier Client")

QUERY = "//body//*[not(self::script) and not(self::style) and not(child::*)]"


class ClassifierClient(object):
    """Classifier for the web elements."""

    def __init__(self, driver):
        """initilize the classifier client"""
        logger.info("Initializing Classifier Client")
        self.driver = driver

    def find_elements_matching_label(self, labeltomatch):
        """finds all page elements matching the label"""
        label = labeltomatch.lower().replace(" ", "")
        logger.info("Finding Elements Matching Label: %s", label)
        all_page_elements = self.driver.find_elements_by_xpath(QUERY)
        logger.debug("Page elements found: %s element", len(all_page_elements))
        elements_found = []
        for element in all_page_elements:
            txt = element.text.lower().replace(" ", "")
            name = element.accessible_name.lower().replace(" ", "")
            if label in name or label in txt:
                logger.debug("Found element: %s", label)
                elements_found.append(element)
        return [WebElement(element.parent,
                           element.id) for element in elements_found]

    def find_text_field_matching_label(self, labeltomatch):
        """finds text fields matching the label"""
        elements = self.find_elements_matching_label(labeltomatch)

        for element in elements:
            if element.aria_role == "textbox":
                return WebElement(element.parent, element.id)

        return None

    def find_button_matching_label(self, labeltomatch):
        """finds buttons matching the label"""
        elements = self.find_elements_matching_label(labeltomatch)
        for element in elements:
            if element.aria_role == "button":
                return WebElement(element.parent, element.id)
        return None

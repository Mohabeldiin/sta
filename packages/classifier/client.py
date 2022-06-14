"""foo"""
from selenium.webdriver.common.by import By

QUERY = "//body//*[not(self::script) and not(self::style) and not(child::*)]"


class ClassifierClient(object):
    """foo"""

    def __init__(self, driver):
        """foo"""
        self.driver = driver

    def find_elements_matching_label(self, label):
        """foo"""
        all_page_elements = self.driver.find_elements(
            by=By.CSS_SELECTOR, value=QUERY)
        elements_found = []
        for element in all_page_elements:
            name = element.accessible_name.lower()
            if label in name:
                elements_found.append(element)
            else:
                txt = element.text.lower()
                if label in txt:
                    elements_found.append(element)
        return elements_found

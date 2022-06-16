"""Setup selenium for the project

    applying BOM Moudel"""

from .driver import setup_selenium_driver, teardown_selenium_driver
from .selenium import (EC, By, WebDriverWait, WebElement, selenium_exceptions,
                       webdriver, unittest)

__all__ = ['setup_selenium_driver', 'teardown_selenium_driver', 'webdriver', 'selenium_exceptions',
           'WebElement', 'By', 'EC', 'WebDriverWait', 'unittest']
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

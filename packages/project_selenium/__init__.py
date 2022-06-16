"""Setup selenium for the project

    applying BOM Moudel"""

from .selenium import webdriver, selenium_exceptions, WebElement
from .driver import setup_selenium_driver

__all__ = ['webdriver', 'selenium_exceptions', 'WebElement']
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

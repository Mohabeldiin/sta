"""Setup selenium for the project

    applying BOM Moudel"""
from packages.logger import project_logger

logger = project_logger("Project Selenium Setup")

try:
    from selenium import webdriver
    from selenium.common import exceptions as selenium_exceptions
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except ImportError:
    logger.error("Selenium is not installed")
    raise ImportError("Please install selenium module") from ImportError

__all__ = ['webdriver', 'selenium_exceptions',
           'WebElement', 'By', 'EC', 'WebDriverWait']
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

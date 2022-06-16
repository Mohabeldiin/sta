"""Setup selenium for the project

    applying BOM Moudel"""
from packages.logger import project_logger

logger = project_logger("Project Selenium Setup")

try:
    from selenium import webdriver
    from selenium.common import exceptions as selenium_exceptions
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logger.error("Selenium is not installed")
    raise ImportError("Please install selenium module") from ImportError

__all__ = ['webdriver','selenium_exceptions','WebElement']
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

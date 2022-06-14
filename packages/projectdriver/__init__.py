"""Setup selenium Chrome driver for the project

    applying BOM Moudel"""
import pathlib
from packages.logger import project_logger

logger = project_logger("Project Driver")

path = pathlib.Path(__file__).parent.resolve()

try:
    from selenium import webdriver
    from selenium.common import exceptions as selenium_exceptions
except ImportError:
    logger.error("Selenium is not installed")
    raise ImportError("Please install selenium module") from ImportError


def setup_selenium_driver() -> webdriver.Chrome:
    """Sets up the selenium driver
        Returns:
            webdriver.Chrome: selenium driver
        Raises:
            WebDriverException: if unable to open selenium driver
            Exception: if unable to open selenium driver"""
    logger.debug("Setting up selenium")
    options = webdriver.ChromeOptions()
    options.headless = False
    try:
        driver = webdriver.Chrome(
            executable_path="chromedriver.exe", options=options)
    except selenium_exceptions.WebDriverException:
        try:
            driver = webdriver.Chrome(
                executable_path=f"{path}\\chromedriver.exe", options=options)
        except selenium_exceptions.WebDriverException as ex:
            logger.critical("Chrome driver not found: %s", ex.__doc__)
            raise (f"Chrome driver not found: {ex.__doc__}") from ex
        except Exception as ex:
            logger.critical("Exception: %s", ex.__doc__)
            raise (f"Exception: {ex.__doc__}") from ex
        else:
            driver.implicitly_wait(5)
            driver.maximize_window()
            logger.debug("Returning driver: %s", driver)
    return driver


__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

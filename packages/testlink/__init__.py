"""Gets the Link from the database

    this file is used as base method for test scripts
    :returns: Link"""
import json

from packages.logger import project_logger
from .validators import url as url_validator

logger = project_logger("Test Link")

try:
    import requests
except ImportError:
    logger.error("Requests is not installed")
    raise ImportError("Please install requests module") from ImportError


def validate_url(url: str) -> str:
    """validate the url
        by removing the http:// or https:// or www.
        Args:
        url (str): url to validate
        Returns:
            str: url without http:// or https:// or www.
        Raises:
            Exception: if url is not string"""
    if url_validator(url):
        logger.info("Valid url: %s", url)
        if url.startswith("http://www."):
            url = url[11:]
        elif url.startswith("http://"):
            url = url[7:]
        elif url.startswith("https://www."):
            url = url[12:]
        elif url.startswith("https://"):
            url = url[8:]
        elif url.startswith("www."):
            url = url[4:]
        if url.endswith("/"):
            url = url[:-1]
        logger.debug("Returning url: %s", url)
    else:
        logger.critical("Invalid url: %s", url)
        raise Exception("Invalid url")
    return url


def get_link_to_test(id:str):
    """Gets the Link from the database and validate it."""
    logger.info("Getting Link from Database")
    return validate_url(get_link_to_test_without_validate(id))


def get_link_to_test_without_validate(id:str):
    """Gets the Link from the database"""
    logger.info("Getting Link from Database")
    # old_link = "https://a5r-testing.herokuapp.com/getLink"
    link = f"https://staapi.herokuapp.com/Url/{id}"
    logger.debug("Requesting Link")
    response = requests.get(link)
    logger.debug("Response Received")
    data = json.loads(response.text)
    logger.debug("Link Received: %s", data['get']['link'])
    logger.info("Link Received")
    return data['get']['link']


__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

"""Gets the Link from the database

    this file is used as base method for test scripts
    :returns: Link"""
import json

from logger import project_logger

logger = project_logger("Test Link")

try:
    import requests
except ImportError:
    logger.error("Requests is not installed")
    raise ImportError("Please install requests module") from ImportError


def get_link_to_test():
    """Gets the Link from the database"""
    logger.info("Getting Link from Database")
    link = "https://a5r-testing.herokuapp.com/getLink"
    logger.debug("Requesting Link")
    response = requests.get(link)
    logger.debug("Response Received")
    data = json.loads(response.text)
    logger.debug("Link Received: %s", data['get'][-1]['link'])
    logger.info("Link Received")
    return data['get'][-1]['link']


__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

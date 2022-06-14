"""Gets the Link from the database

    this file is used as base method for test scripts
    :returns: Link"""
import json
import requests


def get_link():
    """Gets the Link from the database"""
    link = "https://a5r-testing.herokuapp.com/getLink"
    response = requests.get(link)
    data = json.loads(response.text)
    return data['get'][-1]['link']

__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

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


if __name__ == '__main__':
    print(get_link())

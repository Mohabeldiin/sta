"""Api endpoint for the application."""

from flask import Flask
from flask_restful import Api, Resource, http_status_message, reqparse
from packages.websec import WebSec
from packages.speed import SpeedApi
from packages.seo import SEORanking
from packages.logger import setup_logger
from packages.testlink import validate_url

logger = setup_logger("End Point")

class App(Resource):
    """Api endpoint for the application."""

    def __init__(self) -> None:
        """Initialize the app."""
        logger.info("Initializing the app.")
        self.userid = "11111"
        self.name = "mohabelre5m"
        self.city = "maadi"
        logger.info("Initializing the app.")
        self.flask = Flask("API End Point")
        self.api = Api(self.flask)
        logger.debug("Initialized the app.")
        self.api.add_resource(App, "/post", endpoint="post", methods=["post"])
        logger.debug("Added the resource.")

    def post(self) -> str:
        """Post the data."""
        logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        logger.debug("Parsing the data.")
        parser.add_argument('website', type=str,
                            required=True, help="Website is required")
        data = parser.parse_args()
        speed = SpeedApi(validate_url(data["website"]))
        result = speed.get()
        return {'message': http_status_message(200), 'data': result}

    def post_seo(self) -> str:
        """Post the data."""
        logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        logger.debug("Parsing the data.")
        parser.add_argument('website', type=str,
                            required=True, help="Website is required")
        data = parser.parse_args()
        seo = SEORanking(validate_url(data["website"]))
        result_seo = seo.get_result()
        return {'message': http_status_message(200), 'data': result_seo}

    def post_security(self) -> str:
        """post the data"""
        logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        logger.debug("Parsing the data.")
        parser.add_argument('website', type=str,
                            required=True, help="website is required")
        data = parser.parse_args()
        security = WebSec(validate_url(data["website"]))
        result_sec = security()
        return {'message': http_status_message(200), 'data': result_sec}

    def post_all(self) -> str:
        """foo"""
        logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        logger.debug("Parsing the data.")
        parser.add_argument('website', type=str,
                            required=True, help="website is required")
        data = parser.parse_args()
        site_to_test = validate_url(data["website"])
        speed = SpeedApi(site_to_test)
        result_speed = speed.get()
        seo = SEORanking(site_to_test)
        result_seo = seo.get_result()
        security = WebSec(site_to_test)
        result_sec = security()
        result = {
            "speed": result_speed,
            "seo": result_seo,
            "security": result_sec
        }
        return {'message': http_status_message(200), 'data': result}

    def run(self) -> None:
        """Run the app."""
        logger.info("Running the app.")
        self.flask.run(debug=False)

    def __del__(self) -> None:
        """Destructor."""
        logger.info("Destroying the app.")
        del self.userid
        del self.name
        del self.city
        del self.flask
        del self.api
        logger.debug("Destroyed the app.")

if __name__ == '__main__':
    app = App()
    app.run()

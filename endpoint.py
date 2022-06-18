"""Api endpoint for the application."""
import logging

from yaml import parse
from flask import Flask
from flask_restful import Api, Resource, http_status_message, reqparse
from ApiSpeedFinal import Apispeed
from SEO import SEORanking
from websec_immuniweb import Websec

class App(Resource):
    """Api endpoint for the application."""

    def __init__(self) -> None:
        """Initialize the app."""
        self.__logger = self.__setup_loger()
        self.__logger.info("Initializing the app.")
        self.userid = "11111"
        self.name = "mohabelre5m"
        self.city = "maadi"
        self.__logger.info("Initializing the app.")
        self.flask = Flask("API End Point")
        self.api = Api(self.flask)
        self.__logger.debug("Initialized the app.")
        self.api.add_resource(App, "/post", endpoint="post", methods=["post"])
        self.__logger.debug("Added the resource.")

    def post(self)-> str:
        """Post the data."""
        self.__logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        self.__logger.debug("Parsing the data.")
        parser.add_argument('website', type=str, required=True, help="Website is required")
        data = parser.parse_args()
        print(data["website"])
        speed = Apispeed(data["website"])
        result = speed.get()
        return {'message': http_status_message(200), 'data': result}

    def post_seo(self)-> str:
        """Post the data."""
        self.__logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        self.__logger.debug("Parsing the data.")
        parser.add_argument('website', type=str, required=True, help="Website is required")
        data = parser.parse_args()
        print(data["website"])
        seo = SEORanking(data["website"])
        result_seo = seo.get_result()
        return {'message': http_status_message(200), 'data': result_seo}
        
    def post_security(self)-> str:
        """post the data"""
        self.__logger.info("Posting the data.")
        parser = reqparse.RequestParser()
        self.__logger.debug("Parsing the data.")
        parser.add_argument('website', type= str, required=True, help="website is required")
        data = parser.parse_args()
        print(data["website"])
        security = Websec(data["website"])
        result_sec = security.get_result()
        return {'message': http_status_message(200), 'data': result_sec}

    def run(self) -> None:
        """Run the app."""
        self.__logger.info("Running the app.")
        self.flask.run(debug=False)

    @staticmethod
    def __setup_loger() -> logging.Logger:
        """setup the logger
            Log Example:
                2022-05-24 00:45:56,230 - API End Point - INFO: Message
            Returns:
                logging.Logger: logger"""
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG,
            filename='logs/API_endpoint.log',
            filemode="w")
        return logging.getLogger("API End Point")

    def __del__(self) -> None:
        """Destructor."""
        self.__logger.info("Destroying the app.")
        del self.userid
        del self.name
        del self.city
        del self.flask
        del self.api
        self.__logger.debug("Destroyed the app.")
        del self.__logger

if __name__ == '__main__':
    app = App()
    app.run()
"""Temporary Email API Class

    This class is used to get a temporary email address.
    It uses the API provided by https://temp-mail.org/

    Example:
        >>> from temp_mail_api import TempMailAPI
        >>> api = TempMailAPI()
        >>> email = api.get_email()"""

from packages.logger import project_logger

logger  = project_logger("TempMail")

try:
    import json
except ImportError:
    logger.error("json is not installed")
    raise ImportError("Please install json module") from ImportError

try:
    import requests
except ImportError:
    logger.error("requests is not installed")
    raise ImportError("Please install requests module") from ImportError


class _Email(object):
    """Super Class for the TempMail Class
    Attributes:
        email: str of email as Mail@Domain
        Mail: str of Mail
        Domain: str of Domain"""

    def __init__(self):
        """Request for new email
        Return:
            email: str of email as Mail@Domain
            Mail: str of Mail
            Domain: str of Domain"""
        super().__init__()
        logger.info("Initializing TempMail")
        self._api = "https://www.1secmail.com/api/v1/?"
        self._email, self._mail, self._domain = self._creat_new_email()
        logger.info("TempMail initialized with : %s", self._email)

    def _creat_new_email(self):
        """Request for new email
        Return:
            email: str of email as Mail@Domain
            Mail: str of Mail
            Domain: str of Domain"""
        logger.info("Creating new email")
        action = "genRandomMailbox"
        count = 1
        new_mail_request = f"{self._api}action={action}&count={count}"
        new_mail_response = self._request_handler(new_mail_request)
        email = self.__extract_email(new_mail_response)
        mail, domain = email.split("@")
        logger.info("New email created: %s", email)
        return email, mail, domain

    def __extract_email(self, response):
        """Extracting the email from the response
            Args:
                response: requests.Response
            Return:
                email: str of email as Mail@Domain"""
        email = response.text
        for symbol in email:
            if symbol == "[" or symbol == "\"" or symbol == "]":
                email = email.replace(symbol, "")
        logger.info("Extracted email: %s", email)
        return email

    def __try(self, request, exception, count=3):
        """Retry the request for Counter times
        if the request is not successful raises exception
        Args:
            request: str of request
            exception: Exception
            count: int of Counter
        Return:
            response: requests.Response
        Raises:
            exception: Exception"""
        if count:
            try:
                logger.debug("Retrying request: %s", request)
                return requests.get(request)
            except exception as ex:
                logger.error("Exception: %s", ex.__doc__)
                logger.debug("Retrying request: %s", request)
                return self.__try(request, ex, count-1)
        else:
            logger.error("Exception: %s", exception)
            logger.critical("Request failed: %s", request)
            raise exception

    def _request_handler(self, request):
        """Handling the request by retrying the request for Counter times
        if the request is not successful raises exception
        Args:
            request: str of request
        Return:
            response: requests.Response
        Raises:
            exception: Exception"""
        try:
            logger.debug("Requesting: %s", request)
            return requests.get(request)
        except requests.exceptions.ConnectionError as ex:
            logger.debug("ConnectionError: %s", ex.__doc__)
            return self.__try(request, ex)
        except requests.exceptions.Timeout as ex:
            logger.debug("Timeout: %s", ex.__doc__)
            return self.__try(request, ex)
        except requests.exceptions.TooManyRedirects as ex:
            logger.debug("TooManyRedirects: %s", ex.__doc__)
            return self.__try(request, ex)

    def get_mail(self):
        """Get Mail
        Return:
            mail: str of Mail"""
        logger.info("Returning mail: %s", self._mail)
        return self._mail

    def get_domain(self):
        """Get Domain
        Return:
            domain: str of Domain"""
        logger.info("Returning domain: %s", self._domain)
        return self._domain

    def get_email(self):
        """Get Email
        Return:
            email: str of email as Mail@Domain"""
        logger.info("Returning email: %s", self._email)
        return self._email


class TempMail(_Email):
    """TempMail API
    https://www.1secmail.com/api/v1/
    Attributes:
        email: str of email as Mail@Domain
        Mail: str of Mail
        Domain: str of Domain

    Methods:
        get_mail(): str of Mail
        get_domain(): str of Domain
        get_email(): str of email as Mail@Domain
        get_message(): str of message
        get_subject(): str of subject
        receive_mail(): dict of mail"""

    def __init__(self):
        """Initialize Temporary Mail"""
        super().__init__()
        logger.info("Initializing TempMail")

    def __json_handler(self, data):
        """Handling the json data
        Args:
            data: json
        Return:
            message: str of message"""
        try:
            logger.debug("Handling json data: %s", data)
            return json.loads(data)
        except: # pylint: disable=bare-except
            logger.error("Message not found")
            return {}

    def __data_handler(self, data, attribute: str):
        """Handling the data extraction"""
        try:
            return data[0][attribute].strip()
        except: # pylint: disable=bare-except
            try:
                return data[attribute]
            except IndexError as ex:
                logger.error("No attribute found: %s", ex.__doc__)
                return []
            except TypeError as ex:
                logger.error("No attribute found: %s", ex.__doc__)
                return []
            except KeyError as ex:
                logger.error("No attribute found: %s", ex.__doc__)
                return []

    def __last_received_mail(self):
        """Request for the last received mail
        Return:
            response: requests.Response"""
        action = "getMessages"
        mail_request = f"{self._api}action={action}&login={self._mail}&domain={self._domain}"
        logger.debug("Requesting: %s", mail_request)
        mail_response = self._request_handler(mail_request)
        logger.debug(
            "Returning last received mail: %s", mail_response.text)
        return self.__json_handler(mail_response.text)

    def __last_received_id(self):
        """Gets the last mail id
        Return:
            id: int of id"""
        mail = self.__last_received_mail()
        logger.debug("Returning last received id.")
        return self.__data_handler(mail, "id")

    def __last_received_message(self):
        """Request for the last received message
        Return:
            message: str of message"""
        message_id = self.__last_received_id()
        action = "readMessage"
        message_request = f"{self._api}action={action}&login={self._mail}&domain={self._domain}&id={message_id}"
        logger.debug("Requesting: %s", message_request)
        message_response = self._request_handler(message_request)
        logger.debug(
            "Returning last received message: %s", message_response.text)
        return self.__json_handler(message_response.text)

    def __last_received_subject(self):
        """Request for the last received subject
        Return:
            subject: str of subject"""
        message = self.__last_received_message()
        logger.debug("Returning last received subject.")
        return self.__data_handler(message, "subject")

    def __last_received_body(self):
        """Request for the last received body
        Return:
            body: str of body"""
        message = self.__last_received_message()
        logger.debug("Returning last received body.")
        return str(self.__data_handler(message, "textBody"))

    def get_subject(self):
        """Gets the last received subject
        Return:
            subject: str of subject"""
        logger.info("Returning subject: %s",
                          self.__last_received_subject())
        return self.__last_received_subject()

    def get_message(self):
        """Gets the last received body
        Return:
            body: str of body"""
        logger.info("Returning body: %s", self.__last_received_body())
        return self.__last_received_body()

    def receive_mail(self):
        """Receive the last received mail
        Return:
            mail: dict of mail"""
        subject = self.__last_received_subject()
        body = self.__last_received_body()
        received_mail = {
            "subject": subject,
            "body": str(body)
        }
        logger.info("Returning received mail: %s", received_mail)
        return received_mail


if __name__ == '__main__':
    tm = TempMail()
    print(tm.get_email())
    print(tm.get_mail())
    print(tm.get_domain())
    print(tm.get_subject())
    print(tm.get_message())
    print(tm.receive_mail())

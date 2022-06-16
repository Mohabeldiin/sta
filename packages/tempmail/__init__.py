"""Temporary Email API Class

    This class is used to get a temporary email address.
    It uses the API provided by https://temp-mail.org/

    Example:
        >>> from temp_mail_api import TempMailAPI
        >>> api = TempMailAPI()
        >>> email = api.get_email()"""

from .tempmail import TempMail

__all__ = ["TempMail"]
__author__ = "Mohab Mohsen"
__license__ = "MIT"
__email__ = "mohabeldiin@gmail.com"

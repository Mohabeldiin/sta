"""WebSite Security Assessment Tool for Immuniweb.

    This tool is used to assess the security of a website.
    It is based on the OWASP Top 10 and OWASP Mobile Top 10.
    For more info Refer to https://www.immuniweb.com/websec/"""


import time

from packages.logger import project_logger
from packages.project_selenium.driver import (setup_selenium_driver,
                                              teardown_selenium_driver)
from packages.project_selenium.selenium import (EC, By, WebDriverWait,
                                                selenium_exceptions)
from packages.testlink import get_link_to_test

logger = project_logger("WebSec")


class Locators:
    """Defines the locator for the web elements."""
    _IMMUNIWEB = "https://www.immuniweb.com/websec/"
    _URL_TEXTFIELD = (By.XPATH, '//*[@id="httpsearch-url"]')
    _URL_BUTTON = (By.XPATH, '//*[@id="search-input"]/div/span/button')
    _MULTI_IP_FORM = (By.XPATH, '/html/body/div[5]')
    _MULTI_IP_YES_BUTTON = (By.XPATH, '/html/body/div[5]/div[7]/button[1]')
    _SCAN_PROGREC_FORM = (By.XPATH, '/html/body/section/div')
    _SCAN_FINAL_SCORE = (By.XPATH, '//*[@id="mark"]/h5')
    _SCAN_SERVER_IP = (By.XPATH, '//*[@id="server_ip"]')
    _WEB_SOFTWARE_FOUND = (
        By.XPATH, '//*[@id="appscan-stat"]/div/div[1]/div[2]')
    _WEB_SOFTWARE_OUTDATED = (
        By.XPATH, '//*[@id="appscan-stat"]/div/div[2]/div[2]')
    _WEB_SOFTWARE_VULNERABIL = (
        By.XPATH, '//*[@id="appscan-stat"]/div/div[3]/div[2]')


class WebSec(Locators):
    """WebSite Security Assessment Tool"""

    def __init__(self,  url=get_link_to_test()) -> None:
        """Initializes the class"""
        self.__url = url
        self.__driver = setup_selenium_driver()
        self.__open_immuniweb(self._IMMUNIWEB)
        self.__start_scan(self.__url)

    def __del__(self) -> None:
        """Tears down the driver"""
        logger.debug("Tearing down driver")
        teardown_selenium_driver(self.__driver)

    def __open_immuniweb(self, url: str) -> None:
        """Opens the immuniweb page

        Args:
            logger (logging.Logger): logger
            driver (webdriver.Chrome): driver
            url (str): url to open

        Raises:
            TimeoutException: if timeout
            WebDriverException: if chrome driver not found
            Exception: if any other exception"""
        try:
            self.__driver.get(url)
        except selenium_exceptions.TimeoutException as ex:
            logger.critical("TimeoutException: %s", ex.__doc__)
            raise (f"TimeoutException: {ex.__doc__}") from ex
        except selenium_exceptions.WebDriverException as ex:
            logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
            raise (f"Unable to open SE Ranking: {ex.__doc__}") from ex
        except Exception as ex:
            logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
            raise (f"Unable to open SE Ranking: {ex.__doc__}") from ex
        else:
            self.__driver.implicitly_wait(5)

    @ staticmethod
    def __define_text_field(driver, locator):
        """Defines the text field

        Args:
            logger (logging.Logger): logger
            driver (webdriver.Chrome): driver
            locator (tuple): locator

        Returns:
            WebElement: text field
        Raises:
            NoSuchElementException: if text field not found
            Exception: if any other exception"""
        try:
            text_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(locator))
        except selenium_exceptions.NoSuchElementException as ex:
            logger.critical("NoSuchElementException: %s", ex.__doc__)
            raise (f"NoSuchElementException: {ex.__doc__}") from ex
        except selenium_exceptions.TimeoutException as ex:
            logger.critical("TimeoutException: %s", ex.__doc__)
            raise (f"TimeoutException: {ex.__doc__}") from ex
        except Exception as ex:
            logger.critical("Exception: %s", ex.__doc__)
            raise (f"Exception: {ex.__doc__}") from ex
        else:
            logger.debug("Returning text field: %s", text_field)
        return text_field

    @ staticmethod
    def __define_button(driver, locator):
        """Defines the button

        Args:
            logger (logging.Logger): logger
            driver (webdriver.Chrome): driver
            locator (tuple): locator

        Returns:
            WebElement: button
        Raises:
            NoSuchElementException: if button not found
            Exception: if any other exception"""
        try:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator))
        except selenium_exceptions.NoSuchElementException as ex:
            logger.critical("NoSuchElementException: %s", ex.__doc__)
            raise (f"NoSuchElementException: {ex.__doc__}") from ex
        except Exception as ex:
            logger.critical("Exception: %s", ex.__doc__)
            raise (f"Exception: {ex.__doc__}") from ex
        else:
            logger.debug("Returning button: %s", button)
        return button

    @ staticmethod
    def __send_text(text_field, text):
        """Sends text to a text field

        Args:
            logger (logging.Logger): logger
            text_field (WebElement): text field
            text (str): text to send

        Raises:
            Exception: if any exception"""
        try:
            text_field.clear()
            text_field.send_keys(text)
        except Exception as ex:
            logger.critical("Exception: %s", ex.__doc__)
            raise (f"Exception: {ex.__doc__}") from ex

    @ staticmethod
    def __click_button(button):
        """Clicks a button

        Args:
            logger (logging.Logger): logger
            button (WebElement): button

        Raises:
            Exception: if any exception"""
        try:
            button.click()
        except Exception as ex:
            logger.critical("Exception: %s", ex.__doc__)
            raise (f"Exception: {ex.__doc__}") from ex

    def __is_multi_ip(self) -> bool:
        """Checks if the Site is Multi-IP"""
        try:
            logger.debug("Checking if Site have Multi IP")
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(self._MULTI_IP_FORM))
            logger.debug("Site have Multi IP")
            status = True
        except selenium_exceptions.TimeoutException:
            logger.debug("Site don't have Multi IP")
            status = False
        return status

    def __handel_multi_ip(self):
        """Handles Multi IP"""
        if self.__is_multi_ip():
            logger.debug("Handling Multi IP")
            button = self.__define_button(self.__driver,
                                          self._MULTI_IP_YES_BUTTON)
            self.__click_button(button)
        else:
            logger.debug("Site don't have Multi IP")

    def __is_scanning(self) -> bool:
        """foo"""
        try:
            logger.debug("Checking if Site is Scanning")
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(self._SCAN_PROGREC_FORM))
            logger.debug("Still Scanning")
            status = True
        except selenium_exceptions.TimeoutException:
            logger.debug("Fineshed Scanning")
            status = False
        return status

    def __handel_scanning(self):
        """Handles Scanning"""
        if self.__is_scanning():
            logger.debug("Handling Scanning")
            time.sleep(30)
            self.__handel_scanning()
        else:
            logger.debug("Scanning handled")

    def __start_scan(self, url: str):
        """Starts the scan
            Args:
                url (str): url to scan
            Returns:
                dict: scan results
            Raises:
                Exception: if any exception"""
        logger.info("Starting scan for url: %s", url)
        text_field = self.__define_text_field(
            self.__driver, self._URL_TEXTFIELD)
        self.__send_text(text_field, self.__url)
        button = self.__define_button(
            self.__driver, self._URL_BUTTON)
        self.__click_button(button)
        self.__handel_multi_ip()
        self.__handel_scanning()

    def __get_scan_results(self) -> dict:
        """Gets the scan results
            Returns:
                dict: scan results
            Raises:
                Exception: if any exception"""
        logger.info("Getting scan results")
        final_score = self.__handel_get_result(self._SCAN_FINAL_SCORE)
        server_ip = self.__handel_get_result(self._SCAN_SERVER_IP)
        software_found = self.__handel_get_result(self._WEB_SOFTWARE_FOUND)
        software_outdated = self.__handel_get_result(
            self._WEB_SOFTWARE_OUTDATED)
        software_vulnerabil = self.__handel_get_result(
            self._WEB_SOFTWARE_VULNERABIL)
        lib_json = []
        for component in range(1, 3):
            try:
                lib_name = self.__handel_get_result((By.XPATH,
                                                     f'//*[@id="appscan-components-value"]/div[{component}]/div[1]/div[1]'))
                lib_version = self.__handel_get_result((By.XPATH,
                                                        f'//*[@id="appscan-components-value"]/div[{component}]/div[1]/div[2]'))
                lib_message = self.__handel_get_result((By.XPATH,
                                                        f'//*[@id="appscan-components-value"]/div[{component}]/div[2]/div'))
            except selenium_exceptions.NoSuchElementException:
                logger.debug("No such element")
            finally:
                try:
                    lib_vulnerabil_score = []
                    lib_vulnerabil_cve = []
                    lib_vulnerabil_type = []
                    for vuln in range(1, 11):
                        lib_vulnerabil_score.append(self.__handel_get_result((By.XPATH,
                                                                              f'//*[@id="appscan-components-value"]/div[{component}]/div[2]/table/tbody/tr[{vuln}]/td[1]')))
                        lib_vulnerabil_cve.append(self.__handel_get_result((By.XPATH,
                                                                            f'//*[@id="appscan-components-value"]/div[{component}]/div[2]/table/tbody/tr[{vuln}]/td[2]')))
                        typ1 = self.__handel_get_result((By.XPATH,
                                                         f'//*[@id="appscan-components-value"]/div[{component}]/div[2]/table/tbody/tr[{vuln}]/td[3]'))
                        lib_vulnerabil_type.append(typ1)
                except Exception:
                    logger.debug("No such element")
                finally:
                    lib_json_vulnerabil = []
                    for index in range(0, len(lib_vulnerabil_score)):  # pylint: disable = consider-using-enumerate
                        if index == len(lib_vulnerabil_score)-1:
                            lib_json_vulnerabil.append({
                                "score": lib_vulnerabil_score[index],
                                "cve": lib_vulnerabil_cve[index],
                                "type": lib_vulnerabil_type[index]
                            })
                        else:
                            lib_json_vulnerabil.append({
                                "score": lib_vulnerabil_score[index],
                                "cve": lib_vulnerabil_cve[index],
                                "type": lib_vulnerabil_type[index]
                            },)
            if component == 1:
                lib_json.append({
                    "name": lib_name,
                    "version": lib_version,
                    "message": lib_message,
                    "vulnerabil": lib_json_vulnerabil
                },)
            elif component == 2:
                lib_json.append({
                    "name": lib_name,
                    "version": lib_version,
                    "message": lib_message,
                    "vulnerabil": lib_json_vulnerabil
                })
        result = {
            "final_score": final_score,
            "server_ip": server_ip,
            "software_found": software_found,
            "software_outdated": software_outdated,
            "software_vulnerabil": software_vulnerabil,
            "lib_json": lib_json
        }
        logger.debug("Returning scan results: %s", result)
        return result

    def __call__(self,):
        return self.__get_scan_results()

    def __handel_get_result(self, loctor):
        """Handles the result"""
        logger.debug("Handling result")
        try:
            elment = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(loctor))
        except selenium_exceptions.TimeoutException:
            logger.debug("Result not found")
        else:
            logger.debug("Result found")
            results = elment.text
            logger.debug("Result: %s", results)
        return results


if __name__ == "__main__":
    websec = WebSec("https://www.modern-academy.edu.eg/")
    #websec = WebSec("https://www.facebook.com/")
    websec = WebSec()
    print(websec())

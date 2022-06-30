""""SEO Using SE Ranking: seranking.com"""
import arabic_reshaper
from packages.logger import project_logger, get_parser
from packages.project_selenium import (EC, By, WebDriverWait,
                                       selenium_exceptions,
                                       setup_selenium_driver,
                                       teardown_selenium_driver)
from packages.testlink import get_link_to_test

logger = project_logger("SEO")


parser = get_parser()


class SEORanking():
    """SEO Using SE Ranking: seranking.com"""

    # def __init__(self, url: str = get_link_to_test()):
    def __init__(self, args):
        """Initializes seo"""
        url = get_link_to_test(args.id)
        self.driver = setup_selenium_driver()
        api = f"https://online.seranking.com/research.competitor.html/organic/keywords?input={url}&mode=base_domain&source=eg"  # pylint: disable=line-too-long
        self.__open_seranking(api)
        self.__robot_handeler(url)

    def __open_seranking(self, url):
        """Opens the seranking page

        Args:
            logger (logging.Logger): logger
            driver (webdriver.Chrome): driver
            url (str): url to open

        Raises:
            TimeoutException: if timeout
            WebDriverException: if chrome driver not found
            Exception: if any other exception"""
        try:
            self.driver.get(url)
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
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

    def get_organic_traffic(self) -> dict:
        """Extract the organic traffic from the SE Ranking

        Returns:
            dict: {
                "Total traffic": int,
                    "Keywords": int,
                    "Total traffic cost": int,
                    "Backlinks": int
            }

            Raises:
                NoSuchElementException: if element is not found
                WebDriverException: if unable to open SE Ranking
                TimeoutException: if can't find element in time
                Exception: if no organic traffic is found
                """
        try:
            logger.info("Extracting Organic traffic from SE Ranking")
            total_traffic, keyworks, total_traffic_cost, backlinks = self.__get_organic_traffic()
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
            organic_traffic = {
                "Organic traffic": {
                    "Total traffic": total_traffic,
                    "Keywords": keyworks,
                    "Total traffic cost": total_traffic_cost,
                    "Backlinks": backlinks
                }
            }
            logger.debug(
                "Returning Organic traffic: %s", organic_traffic)
        return organic_traffic

    def __get_organic_traffic(self) -> dict:
        """Extracts Organic Traffic

        Returns:
            "Total traffic": int,
            "Keywords": int,
            "Total traffic cost": int,
            "Backlinks": int

        Raises:
            NoSuchElementException: if element is not found
            WebDriverException: if unable to open SE Ranking
            Exception: if no organic traffic is found"""
        try:
            elements = WebDriverWait(
                self.driver, timeout=5).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "keywords-traffic-chart-tab__value")))
        except selenium_exceptions.NoSuchElementException as ex:
            logger.critical("NoSuchElementException: %s", ex.__doc__)
            raise (f"NoSuchElementException: {ex.__doc__}") from ex
        except selenium_exceptions.WebDriverException as ex:
            logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
            raise (f"Unable to open SE Ranking{ex.__doc__}") from ex
        except Exception as ex:
            logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
            raise (f"Unable to open SE Ranking{ex.__doc__}") from ex
        else:
            total_traffic = elements.pop(0).text
            keyworks = elements.pop(0).text
            total_traffic_cost = elements.pop(0).text
            backlinks = elements.pop(0).text
            logger.debug("Returning Organic traffic values")
        return total_traffic, keyworks, total_traffic_cost, backlinks

    def get_keywords(self):
        """foo"""
        logger.info("Attempting to Extract keywords from SE Ranking")
        keywords = self.__get_keywords()
        logger.debug("Returning keywords: %s", keywords)
        result = {
            "1": keywords[0],
            "2": keywords[1],
            "3": keywords[2],
            "4": keywords[3],
            "5": keywords[4],
            "6": keywords[5],
            "7": keywords[6],
            "8": keywords[7],
            "9": keywords[8],
            "10": keywords[9]
        }
        logger.debug("Returning result: %s", result)
        return result

    def __get_keywords(self):
        """Extracts keywords

        Returns:
            list: list of keywords

        Raises:
            NoSuchElementException: if element is not found
            WebDriverException: if unable to open SE Ranking
            Exception: if no keywords are found"""
        keywords = []
        for index in range(1, 11):
            try:
                element = WebDriverWait(
                    self.driver, timeout=100).until(
                        EC.presence_of_element_located(
                            (By.XPATH, f'//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div/table/tbody/tr[{str(index)}]/td[1]/div/div/div[2]/div/a')))  # pylint: disable=line-too-long
            except selenium_exceptions.NoSuchElementException as ex:
                logger.critical("NoSuchElementException: %s", ex.__doc__)
                raise (f"NoSuchElementException: {ex.__doc__}") from ex
            except selenium_exceptions.WebDriverException as ex:
                logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
                raise (f"Unable to open SE Ranking{ex.__doc__}") from ex
            except Exception as ex:
                logger.critical("Unable to open SE Ranking: %s", ex.__doc__)
                raise (f"Unable to open SE Ranking{ex.__doc__}") from ex
            else:
                keyword = element.text
                character = keyword[2]
                if('\u0600' <= character <= '\u06FF' or
                    '\u0750' <= character <= '\u077F' or
                    '\u08A0' <= character <= '\u08FF' or
                    '\uFB50' <= character <= '\uFDFF' or
                    '\uFE70' <= character <= '\uFEFF' or
                    '\U00010E60' <= character <= '\U00010E7F' or
                        '\U0001EE00' <= character <= '\U0001EEFF'):
                    keyword = arabic_reshaper.reshape(keyword)[::-1]
                keywords.append(keyword)
                logger.debug("Keyword: %s", keyword)
        return keywords

    def __robot_handeler(self, url: str):
        """Handles Google reCaptcha

        Args:
            url (str): url to be opened

        Raises:
            Exception: if unable to Handel reCaptcha"""
        try:
            if WebDriverWait(self.driver, timeout=5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-popup__body"))):
                logger.info("Robot handeler found")
                self.driver.refresh()
                self.__robot_handeler(url)
        except selenium_exceptions.TimeoutException:
            logger.info("Robot handeler not found")
            return
        except Exception as ex:
            logger.critical(
                "Unable to to handle Google Robotes: %s", ex.__doc__)
            raise (f"Unable to to handle Google Robotes: {ex.__doc__}") from ex

    def get_result(self):
        """Gets the result of the search"""
        logger.info("Attempting to Extract result from SE Ranking")
        organic_traffic = self.get_organic_traffic()
        keywords = self.get_keywords()
        result = {
            "Organic traffic": organic_traffic,
            "Keywords": keywords
        }
        logger.debug("Returning result: %s", result)
        return result

    def __del__(self):
        """Tears down the driver"""
        logger.debug("Tearing down driver")
        teardown_selenium_driver(self.driver)
        logger.debug("Tear Down Successfully.")


if __name__ == '__main__':
    # seo = SEORanking("https://www.google.com")
    seo = SEORanking(parser.parse_args())
    print(seo.get_result())
    del seo

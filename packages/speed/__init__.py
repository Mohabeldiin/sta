"""Interactes with Google PageSpeed Insights API"""

import json
import urllib.request

from packages.logger import setup_logger

logger = setup_logger("Speed API")


class SpeedApi:
    """Speed API

    Args:
        website: website to be tested

    Returns:
        data: data from the API"""

    def __init__(self, website: str):
        """Initialize Speed API"""
        logger.info("Initializing Speed API")
        url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={website}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU"  # pylint: disable=line-too-long
        with urllib.request.urlopen(url) as response:
            self.data = json.loads(response.read())

    def __loading_experiemnce(self):
        """Loading Experience"""
        fcp = self.data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data["loadingExperience"]["overall_category"]

        data_le = {
            "fcp": fcp,
            "fid": fid,
            "lcp": lcp,
            "cls": cls,
            "overall": overall
        }
        return data_le

    def __origin_loading_experience(self):
        """Origin Loading Experience"""
        fcp = self.data["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data["originLoadingExperience"]["overall_category"]

        data_ole = {
            "fcp": fcp,
            "fid": fid,
            "lcp": lcp,
            "cls": cls,
            "overall": overall
        }
        return data_ole

    def __lighthouse_result(self):
        """Lighthouse Result"""
        fcp = self.data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
        tto = self.data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
        lcp = self.data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
        cls = self.data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
        tbt = self.data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
        si = self.data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]

        data_lhr = {
            "fcp": fcp,
            "tto": tto,
            "lcp": lcp,
            "cls": cls,
            "tbt": tbt,
            "si": si
        }
        return data_lhr

    def __overall(self):
        overall_performance = self.data["lighthouseResult"]["categories"]["performance"]["score"] * 100

        data_all_performance = {
            "overall_performance": overall_performance
        }
        return data_all_performance

    def get(self):
        """Get data from the API"""
        data = {
            "loadingExperience": self.__loading_experiemnce(),
            "originLoadingExperience": self.__origin_loading_experience(),
            "lighthouseResult": self.__lighthouse_result(),
            "overall": self.__overall()
        }
        return data


if __name__ == "__main__":
    app = SpeedApi("https://www.google.com")
    print(app.get())

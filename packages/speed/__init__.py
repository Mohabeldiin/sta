"""Interactes with Google PageSpeed Insights API"""

import json
# import urllib.request
import requests

from packages.logger import setup_logger, get_parser
from packages.testlink import get_link_to_test_without_validate

logger = setup_logger("Speed API")


parser = get_parser()


class SpeedApi:
    """Speed API

    Args:
        website: website to be tested

    Returns:
        data1: data1 from the API"""

    def __init__(self, args):
        """Initialize Speed API"""
        logger.info("Initializing Speed API")
        self.id = args['id']
        website = get_link_to_test_without_validate(self.id)
        url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={website}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU"  # pylint: disable=line-too-long
        # with urllib.request.urlopen(url) as response:
        with requests.get(url) as response:
            self.data1 = json.loads(response.text)

    def __loading_experiemnce(self):
        """Loading Experience"""
        fcp = self.data1["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data1["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data1["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data1["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data1["loadingExperience"]["overall_category"]

        data1_le = {
            "fcp": fcp,
            "fid": fid,
            "lcp": lcp,
            "cls": cls,
            "overall": overall
        }
        return data1_le

    def __origin_loading_experience(self):
        """Origin Loading Experience"""
        fcp = self.data1["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data1["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data1["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data1["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data1["originLoadingExperience"]["overall_category"]

        data1_ole = {
            "fcp": fcp,
            "fid": fid,
            "lcp": lcp,
            "cls": cls,
            "overall": overall
        }
        return data1_ole

    def __lighthouse_result(self):
        """Lighthouse Result"""
        fcp = self.data1["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
        tto = self.data1["lighthouseResult"]["audits"]["interactive"]["displayValue"]
        lcp = self.data1["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
        cls = self.data1["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
        tbt = self.data1["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
        si = self.data1["lighthouseResult"]["audits"]["speed-index"]["displayValue"]

        data1_lhr = {
            "fcp": fcp,
            "tto": tto,
            "lcp": lcp,
            "cls": cls,
            "tbt": tbt,
            "si": si
        }
        return data1_lhr

    def __overall(self):
        overall_performance = self.data1["lighthouseResult"]["categories"]["performance"]["score"] * 100

        data1_all_performance = {
            "overall_performance": overall_performance
        }
        return data1_all_performance

    def get(self):
        """Get data1 from the API"""
        loadingExperience = self.__loading_experiemnce()
        originLoadingExperience = self.__origin_loading_experience()
        lighthouseResult = self.__lighthouse_result()
        overall = self.__overall()
        data1 = {
            "loadingExperince": str(loadingExperience['overall']),
            "LE_FCP": str(loadingExperience['fcp']),
            "LE_FID": str(loadingExperience['fid']),
            "LE_CLS": str(loadingExperience['cls']),
            "LE_LCP": str(loadingExperience['lcp']),
            "OriginLoadingExperince": str(originLoadingExperience['overall']),
            "OLE_FCP": str(originLoadingExperience['fcp']),
            "OLE_FID": str(originLoadingExperience['fid']),
            "OLE_CLS": str(originLoadingExperience['cls']),
            "OLE_LCP": str(originLoadingExperience['lcp']),
            "LH_TBT": str(lighthouseResult['tbt']),
            "LH_SI": str(lighthouseResult['si']),
            "LH_FCP": str(lighthouseResult['fcp']),
            "LH_TTI": str(lighthouseResult['tto']),
            "LH_CLS": str(lighthouseResult['cls']),
            "LH_LCP": str(lighthouseResult['lcp']),
            "PR_Precentage": str(overall['overall_performance']),
            "LinkOwner": str(self.id)}
        return data1


if __name__ == "__main__":
    # app = SpeedApi("https://www.google.com")
    app = SpeedApi({'id': '62bceb22c08164c7e7ce9ad5'})
    # args.id = "62bceb22c08164c7e7ce9ad5"
    # app = SpeedApi("--id 62bceb22c08164c7e7ce9ad5")
    print(app.get())

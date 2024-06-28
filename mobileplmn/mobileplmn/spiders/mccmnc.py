import scrapy
from bs4 import BeautifulSoup

from ..items import MobileplmnItem


class MccmncSpider(scrapy.Spider):
    name = "mccmnc"
    allowed_domains = ["www.mcc-mnc.com"]
    start_urls = ["https://www.mcc-mnc.com"]

    def parse(self, response, *args, **kwargs):
        print("response")
        soup = BeautifulSoup(response.body, 'html.parser')
        tb_items = soup.select("#mncmccTable tr")
        print(len(tb_items))
        for tb_item in tb_items[1:]:
            tr_items = tb_item.select("td")
            mobileplmn = MobileplmnItem()
            mobileplmn["mcc"] = tr_items[0].text
            mobileplmn["mnc"] = tr_items[1].text
            mobileplmn["iso"] = tr_items[2].text
            mobileplmn["country"] = tr_items[3].text
            mobileplmn["country_code"] = tr_items[4].text
            mobileplmn["network"] = tr_items[5].text
            # print(mobileplmn)
            yield mobileplmn
        pass

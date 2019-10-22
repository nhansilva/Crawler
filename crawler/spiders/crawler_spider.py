from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    start_urls = [

        "https://vietnamnet.vn/vn/the-thao/",
    ]

    def parse(self, response):
        questions = Selector(response).xpath(
            '//div[@class="box-subcate-content list-content-loadmore clearfix"]/div[@class="box-subcate-style4 m-b-20 '
            'clearfix"]')

        for question in questions:
            item = CrawlerItem()

            item['Title'] = question.xpath(
                'div[@class="box-subcate-style4-caption"]/h3[@class="box-subcate-style4-title"]/a/text()').get()
            item['ImageURL'] = question.xpath(
                'a/img/@src').get()
            item['League'] = question.xpath(
                'div[@class="box-subcate-style4-caption"]/a[@class="box-subcate-style4-namecate m-t-5 m-b-5"]/text()').get()
            item['Description'] = question.xpath(
                'div[@class="box-subcate-style4-caption"]/div[@class="f-14 box-subcate-style4-lead lead"]/text()').get()
            yield item

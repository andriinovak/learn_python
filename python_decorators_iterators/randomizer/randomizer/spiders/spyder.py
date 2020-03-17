# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
# from response.meta import RawResponseItem


class SpyderSpider(scrapy.Spider):
    name = 'spyder'
    allowed_domains = []
    start_urls = ['http://www.random.org/lists/']

    def parse(self, response):
        formdata = {'list': 'first\r\nsecond\r\nfive\r\nsix'}
        yield FormRequest.from_response(response,
                                        formnumber=1,
                                        formdata=formdata,
                                        clickdata={'type': 'submit'},
                                        callback=self.get_results)

    def get_results(self, response):
        item = {}
        # populated from response.meta

        # capture raw response
        # populated from response.meta
        # item['appid'] = response.meta['appid']
        # item['crawlid'] = response.meta['crawlid']
        # item['attrs'] = response.meta['attrs']

        # populated from raw HTTP response
        # item["url"] = response.request.url
        item["response_url"] = response.url
        # item["body"] = response.body
        item["status_code"] = response.status
        item["result"] = []
        for i in response.xpath('/html/body/div/ol/li'):
            text = i.xpath('text()').extract()
            print(text)
            item["result"].extend(text)

        print(item["result"])
        yield item


"""terminal command save dict to file"""
# python -m scrapy crawl spyder -o output.json -t json

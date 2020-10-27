# # -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']

    # User agent of your currect version of chrome
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div//article[@class='product_pod']"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'book_name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("//div/p[@class='price_color']/text()").get(),
            # 'user-agent': response.request.header['User-agent']
        }


#Solution :
# -*- coding: utf-8 -*-
#########################################################################
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BooksSpider(CrawlSpider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com']

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True),
#         Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
#     )

#     def parse_item(self, response):
#         yield {
#             'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
#             'price': response.xpath("(//div[@class='col-sm-6 product_main']/p)[1]/text()").get()
#         }
#########################################################################

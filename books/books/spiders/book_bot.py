# -*- coding: utf-8 -*-
import scrapy
from ..items import BooksItem

class BookBotSpider(scrapy.Spider):
    name = 'book_bot'
    allowed_domains = ['goodreads.com']
    start_urls = ['http://www.goodreads.com/list/show/312.Best_Humorous_Books/']

    def parse(self, response):
        item=BooksItem()
        li=['HUMOROUS BOOKS']
        bookTitle=response.xpath('//a[@class="bookTitle"]/span/text()').extract()
        authorName=response.xpath('//a[@class="authorName"]/span/text()').extract()
        rating=response.xpath('//span[@class="minirating"]/text()').extract()
        category=li

        
        item['bookTitle']= bookTitle
        item['authorName']= authorName
        item['rating']= rating
        item['category']=category

        yield item

        next_page = response.xpath('//a[@class="next_page"]/@href').get()

        req = scrapy.Request(url='http://www.goodreads.com'+next_page ,callback=self.parse)
        yield req

        print(next_page)








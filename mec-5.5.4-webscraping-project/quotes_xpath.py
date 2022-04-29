import scrapy


class QuotesCssSpider(scrapy.Spider):
    name = 'quotes_css'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('.//div[@class="quote"]'):
            yield {
                'text': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//a[@class="tag"]/text()').getall(),
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)

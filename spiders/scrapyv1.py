
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.loader import ItemLoader
from benimproject.items import Test1Item
#############################################################################

class MySpider(CrawlSpider):
    name = 'son'
    allowed_domains = ['turkomp.gov.tr']
    start_urls = ['http://www.turkomp.gov.tr/food-300']



    def parse(self, response):

        loader = ItemLoader(item=Test1Item(), response=response)

        loader.add_xpath("Kod", "/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()")
        loader.add_value(None, {'Kod': 'x',})
        loader.add_xpath("Gida", "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/label/text()")
        loader.add_value(None, {'Gida': 'x',})
        loader.add_xpath("B_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[3]/div[2]/text()")
        loader.add_value(None, {'B_isim': 'x',})
        loader.add_xpath("Y_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[4]/div[2]/text()")
        loader.add_value(None, {'Y_isim': 'x',})
        loader.add_xpath("Grup", "/html/body/div[2]/div[3]/div/div[2]/div/div[5]/div[2]/a/text()")
        loader.add_value(None, {'Grup': 'x',})
        #responseloader.add_xpath("l_code", '/html/body/div[2]/div[3]/div/div[2]/div/div[6]/div[2]/a/text()')
        loader.add_xpath("azot", '/html/body/div[2]/div[3]/div/div[2]/div/div[7]/div[2]/text()')
        loader.add_value(None, {'azot': 'x',})
        loader.add_xpath("ydo", '/html/body/div[2]/div[3]/div/div[2]/div/div[8]/div[2]/text()')
        loader.add_value(None, {'ydo': 'x',})
        #quote_item = loader.load_item()

        #Id = response.css("div.col-sm-8::text").extract_first()
        #Id = response.css("div.col-sm-8::text").extract_first()
        # print(Id
        yield loader.load_item()
"""
        table = response.xpath('//*[@id="foodResultlist"]/tbody/tr')
        for row in table:
            yield {
                'Id': Id,
                'birlesen': row.xpath('td[1]/a/text()').extract_first(),
                'birim': row.xpath('td[2]/text()').extract_first(),
                'ortalama': row.xpath('td[3]/a/text()').extract_first(),
                'min_t': row.xpath('td[4]/text()').extract_first(),
                'max_t': row.xpath('td[5]/text()').extract_first(),
            }


        table = response.xpath('//*[@id="foodResultlist"]/tbody/tr')
        for row in table:
            #loader = ItemLoader(item=quote_item, selector=row)
            loader.add_value('Id_kod', Id)
                loader.add_xpath('birlesen','td[1]/a/text()')
            loader.add_row.xpath('birim', 'td[2]/a/text()')
            loader.add_xpath('ortalama', 'td[3]/text()')
            loader.add_xpath('min_t', 'td[4]/text()')
            loader.add_xpath('max_t', 'td[5]/text()')
        yield loader.load_item()

"""

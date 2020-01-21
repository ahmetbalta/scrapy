from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from benimproject.items import Test


class DemoSpider(CrawlSpider):
    name = "icerik"
    allowed_domains = ["www.turkomp.gov.tr"]
    start_urls = ["http://www.turkomp.gov.tr/database"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=("//*[@id=\"mydatalist\"]/tbody/tr/td[1]")),
             callback='parse_item'),
    )
    def parse_item(self, response):
       tkod = response.xpath("/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()").get()
       table = response.xpath('//*[@id="foodResultlist"]/tbody/tr')
       for quote in table:
           loader = ItemLoader(item=Test(), selector=quote)
           loader.add_value("t_Id", tkod)

           loader.add_xpath('birlesen', "td[1]/a/text()")

           loader.add_xpath('birim', "td[2]/text()")

           loader.add_xpath('ortalama', "td[3]/a/text()")
           loader.add_xpath('min_t', "td[4]/text()")
           loader.add_xpath('max_t', "td[5]/text()")


           yield loader.load_item()


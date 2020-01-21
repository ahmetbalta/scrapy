import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from benimproject.items import Test1Item

class DemoSpider(CrawlSpider):
   name = "demo"
   allowed_domains = ["www.turkomp.gov.tr"]
   start_urls = ["http://www.turkomp.gov.tr/database"]
      
   rules = ( 
      Rule(LinkExtractor(allow =(), restrict_xpaths = ("//*[@id=\"mydatalist\"]/tbody/tr/td[1]")),
         callback = 'parse_item'),
   )

   def parse_item(self, response):

       tkod = response.xpath("/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()").get()
       table = response.xpath('//*[@id="foodResultlist"]/tbody/tr')
       for quote in table:

           loader = ItemLoader(item=Test1Item(), selector=quote)
           loader.add_value("t_Id", tkod)

           loader.add_xpath('birlesen', "td[1]/a/text()")

           loader.add_xpath('birim', "td[2]/text()")

           loader.add_xpath('ortalama', "td[3]/a/text()")
           loader.add_xpath('min_t', "td[4]/text()")
           loader.add_xpath('max_t', "td[5]/text()")
           item = loader.load_item()

       loader = ItemLoader(item=item, response=response)
       loader.add_xpath("Kod", "/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()")
       loader.add_value(None, {'Kod': 'x', })
       loader.add_xpath("Gida", "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/label/text()")
       loader.add_value(None, {'Gida': 'x', })
       loader.add_xpath("B_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[3]/div[2]/text()")
       loader.add_value(None, {'B_isim': 'x', })
       loader.add_xpath("Y_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[4]/div[2]/text()")
       loader.add_value(None, {'Y_isim': 'x', })
       loader.add_xpath("Grup", "/html/body/div[2]/div[3]/div/div[2]/div/div[5]/div[2]/a/text()")
       loader.add_value(None, {'Grup': 'x', })
       # responseloader.add_xpath("l_code", '/html/body/div[2]/div[3]/div/div[2]/div/div[6]/div[2]/a/text()')
       loader.add_xpath("azot", '/html/body/div[2]/div[3]/div/div[2]/div/div[7]/div[2]/text()')
       loader.add_value(None, {'azot': 'x', })
       loader.add_xpath("ydo", '/html/body/div[2]/div[3]/div/div[2]/div/div[8]/div[2]/text()')
       loader.add_value(None, {'ydo': 'x', })
       yield loader.load_item()


"""
   def parse_item(self, response):
      loader = ItemLoader(item=Test1Item(), response=response)
      loader.add_xpath("Kod", "/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()")
      loader.add_value(None, {'Kod': 'x', })
      loader.add_xpath("Gida", "/html/body/div[2]/div[3]/div/div[2]/div/div[1]/label/text()")
      loader.add_value(None, {'Gida': 'x', })
      loader.add_xpath("B_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[3]/div[2]/text()")
      loader.add_value(None, {'B_isim': 'x', })
      loader.add_xpath("Y_isim", "/html/body/div[2]/div[3]/div/div[2]/div/div[4]/div[2]/text()")
      loader.add_value(None, {'Y_isim': 'x', })
      loader.add_xpath("Grup", "/html/body/div[2]/div[3]/div/div[2]/div/div[5]/div[2]/a/text()")
      loader.add_value(None, {'Grup': 'x', })
      # responseloader.add_xpath("l_code", '/html/body/div[2]/div[3]/div/div[2]/div/div[6]/div[2]/a/text()')
      loader.add_xpath("azot", '/html/body/div[2]/div[3]/div/div[2]/div/div[7]/div[2]/text()')
      loader.add_value(None, {'azot': 'x', })
      loader.add_xpath("ydo", '/html/body/div[2]/div[3]/div/div[2]/div/div[8]/div[2]/text()')
      loader.add_value(None, {'ydo': 'x', })
      item = loader.load_item()
      tkod = response.xpath("/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/text()").get()
      table = response.xpath('//*[@id="foodResultlist"]/tbody/tr')
      for quote in table:
          loader = ItemLoader(item=item, selector=quote)
          loader.add_value("t_Id", tkod)
          loader.add_xpath('birlesen', "td[1]/a/text()")
          loader.add_xpath('birim', "td[2]/text()")
          loader.add_xpath('ortalama', "td[3]/a/text()")
          loader.add_xpath('min_t', "td[4]/text()")
          loader.add_xpath('max_t', "td[5]/text()")
          yield loader.load_item()
         
   
      for row in table:
          loader = ItemLoader(item=Test1Item(), selector=row)
          loader.add_xpath('birlesen', 'td[1]/a/text()')
          loader.add_value(None, {'birlesen': 'x', })
          loader.add_xpath('birim', 'td[2]/text()')
          loader.add_value(None, {'birim': 'x', })
          loader.add_xpath('ortalama', 'td[3]/a/text()')
          loader.add_value(None, {'ortalama': 'x', })
          loader.add_xpath('min_t', 'td[4]/text()')
          loader.add_value(None, {'min_t': 'x', })
          loader.add_xpath('max_t', 'td[5]/text()')
          loader.add_value(None, {'max_t': 'x', })

          return loader.load_item()


"""
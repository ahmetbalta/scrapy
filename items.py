## -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def remove_quotes(text):
    # strip the unicode quotes
    #text = text.strip(u'\u201c'u'\u201d')
    text = text.strip()
     
    return text

class Test1Item(Item):
    # define the fields for your item here like:

    Kod = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor = TakeFirst()
    )
    Gida = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor = TakeFirst()
    )
    Grup = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor = TakeFirst()
    )


    B_isim = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    Y_isim = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    #l_code = Field(
    #    input_processor=MapCompose(remove_quotes),
    #    output_processor=TakeFirst()
    #)
    azot = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    ydo = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )

class Test(Item):
    t_Id = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )

    birlesen = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )


    birim = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    ortalama = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    min_t = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    max_t = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )


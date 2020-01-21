# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES settingr
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from benimproject.models import Tanim, Kategori, db_connect, create_table, Icerik_Index
import logging

class BenimprojectPipeline(object):
    def __init__(self):
        """
               Initializes database connection and sessionmaker
               Creates tables
               """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()

        index = Kategori()
        Gida = Tanim()
        #Icerik = Icerik_Index()

        index.grub = item["Grup"]

        Gida.Turkomp = item['Kod']
        Gida.Gida_Name = item["Gida"]
        Gida.Gida_Grup =item["Grup"]
        Gida.Bilim_Name=item["B_isim"]
        Gida.Yore_Name = item["Y_isim"]
        #Gida_Index.Langual_Cade = item["l-code"]
        Gida.Azot_D_F = item['azot']
        Gida.Yag_D_F = item['ydo']


        #exist = session.query(Kategori).filter_by(Kategori.grub= index.grub).first()
        exist = session.query(Kategori).filter_by(grub=item["Grup"]).first()
        if exist is None:
            Gida.grub.append(index)
        try:
            session.add(Gida)
            #session.add(Gida)
            #session.add(Icerik)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            #session.flush()
            session.close()

        return item


class IcerikPipeline(object):
    def __init__(self):
        """
               Initializes database connection and sessionmaker
               Creates tables
               """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()

        Icerik = Icerik_Index()

        Icerik.Birlesen_Id = item["t_Id"]
        Icerik.Birlesen_Name = item["birlesen"]
        Icerik.Birlesen_Birim = item["birim"]
        Icerik.Birlesen_Averaz_D = item["ortalama"]
        Icerik.Birlesen_Min_D = item["min_t"]
        Icerik.Birlesen_Max_D = item["max_t"]



        try:

            session.add(Icerik)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            # session.flush()
            session.close()

        return item


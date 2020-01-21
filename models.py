from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():


    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)
    
bag = Table('bag', Base.metadata, 
    Column('index_id', Integer, ForeignKey('index.Id')),
    Column('gidaid', Integer, ForeignKey('Gida_Index.Gida_Id'))
)

class Kategori(Base):
    __tablename__ = "index"

    Id = Column('Id', Integer, autoincrement=True, primary_key = True)
    grub = Column('grub', String(150))
    tanim = relationship('Tanim', secondary='bag')

 

class Tanim(Base):
    __tablename__ = "Gida_Index"
    Gida_Id = Column('Gida_Id', Integer, autoincrement=True, primary_key=True)

    Turkomp = Column('Turkomp', String(20), nullable=True)
    Gida_Name = Column('Gida_Name', String(100), nullable=True)
    Gida_Grup = Column('Gida_Grup', String(150), nullable=True)
    Bilim_Name = Column('Bilim_Name', String(100), nullable=True)
    Yore_Name = Column('Yore_Name', String(100), nullable=True)
    #Langual_Code = Column('Langual_Code', String)
    Azot_D_F = Column('Azot_D_F', String(10), nullable=True)
    Yag_D_F = Column('Yag_D_F', String(10), nullable=True)
    grub = relationship('Kategori', secondary ='bag')


class Icerik_Index(Base):
    __tablename__ = "Icerik"
    Icerik_Id = Column('Icd', Integer, primary_key=True)
    Birlesen_Id = Column('Turkomp', String(20))
    Birlesen_Name = Column('Birlesen_Name', String(100))
    Birlesen_Birim = Column('Birlesen_Birim', String(10))
    Birlesen_Averaz_D = Column('Birlesen_Averaz_D', String)
    Birlesen_Min_D = Column('Birlesen_Min_D', String)
    Birlesen_Max_D = Column('Birlesen_Max_D', String)



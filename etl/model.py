import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sql
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Boolean,
    Enum,
    BigInteger,
    # pr,
    DECIMAL,
    Date
)
from sqlalchemy.sql import func
from database import  Base, engine, _add_tables
from sqlalchemy.ext.declarative import declarative_base

# Define the DIM_DEVICE_DIRECTORY table
class DIM_DEVICE_DIRECTORY(Base):

    __tablename__ = 'DEVICE_DIRECTORY'

    TAC = Column(Integer, nullable=False, primary_key=True)
    MODEL_NAME = Column(String(200), nullable=False)
    VENDOR_NAME = Column(String(200), nullable=False)
    SUPPORTS_LTE = Column(Integer, nullable=False)
    SUPPORTS_VOLTE = Column(Integer, nullable=False)
    BATTERY_CAPACITY = Column(DECIMAL(9,2), nullable=False)
    BATTERY_TYPE = Column(String(50), nullable=False)
    BODY_DEPTH = Column(DECIMAL(9, 2), nullable=False)
    BODY_HEIGHT = Column(DECIMAL(9, 2), nullable=False)
    BODY_WIDTH = Column(DECIMAL(9, 2), nullable=False)
    BODY_TYPE = Column(String(50), nullable=False)
    OS_TYPE = Column(String(50), nullable=False)
    OS_VENDOR = Column(String(100), nullable=False)
    CAMERA_FLASHLIGHT = Column(Integer, nullable=False)
    SUPPORTS_MULTISIM = Column(Integer, nullable=False)
    SUPPORTS_ESIM = Column(Integer, nullable=False)
    SUPPORT_5G = Column(Integer, nullable=False)
    SIM_COUNT = Column(Integer, nullable=False)
    CPU_CORES = Column(Integer, nullable=False)
    MULTISIM_MODE = Column(String(50), nullable=False)
    PIXEL_DENSITY = Column(DECIMAL(9,2), nullable=False)
    RAM_SIZE = Column(DECIMAL(9,2), nullable=False)
    RELEASE_DATE = Column(Date, nullable=False)
    BAND_1800 = Column(Integer, nullable=False)
    BAND_1900 = Column(Integer, nullable=False)
    BAND_850 = Column(Integer, nullable=False)
    BAND_900 = Column(Integer, nullable=False)

class DIM_SUB_DEVICE_DIRECTORY(Base):

    __tablename__ = 'SUB_DEVICE_DIRECTORY'

    INDEX = Column(Integer, primary_key=True, nullable=False)
    ID = Column(Integer, nullable=False)
    DEVICE_ID = Column(Integer, ForeignKey('DEVICE_DIRECTORY.TAC'), nullable=False)
    BRAND = Column(String(100), nullable=False)
    MODEL = Column(String(200), nullable=False)
    NETTYPE = Column(String(50), nullable=False)
    OS = Column(String(50), nullable=False)
    START_DATE = Column(Date, nullable=False)
    END_DATE = Column(Date, nullable=False)
    DAYS_USED = Column(Integer, nullable=False)
    AVG_DAYS_USED = Column(DECIMAL(9,2), nullable=False)

recreate = True

if recreate:
    Base.metadata.drop_all(engine)
    print('The Schema is deleted')
    Base.metadata.create_all(bind=engine)
    print('new schema is created')
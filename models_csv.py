#!/usr/bin/python3
"""DataSession and DataInterval models for the MySQL tables"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Float

Base = declarative_base()

class DataSession(Base):
    """Class for the session data of the ev_charger"""

    __tablename__ = "session"
    # This could be transformed in a uuid
    SessionID = Column(Integer, primary_key=True)
    VendorID = Column(String(30))
    LocationID = Column(String(30))
    EVSEID = Column(String(30))
    PortID = Column(String(30))
    EVSEModelNbr = Column(String(30))
    EVSENbrOfPorts = Column(Integer)
    SessionStartDateTime = Column(DateTime)
    SessionEndDateTime = Column(DateTime)
    SessionConnectionTime = Column(Integer)
    Duration_StateC = Column(Integer)
    # For the next 3 lines, we might need to adjust the precision, depending on the wanted results
    SessionKWH = Column(Float)
    SessionMaxDemandKW = Column(Float)
    SessionAverageDemandKWH = Column(Float)
    # This a string for now because of the $ they put in front, but it might be good to ask Kitu
    # to remove it so we change it to float
    SessionSaleAmount = Column(String(30))
    VehicleMake = Column(String(30))
    VehicleModel = Column(String(30))
    # This could be an Integer, or a uuid
    UserID = Column(String(30))
    DREventCalled = Column(String(30))
    DREventParticipated = Column(String(30))

class Interval(Base):
    """Class for the interval data of the ev_charger
    The name of the table is intentionally intervall with two l
    because the word interval was reserved in mysql"""

    __tablename__ = "intervall"
    # This could be transformed in a uuid
    IntervalID = Column(Integer, primary_key=True)
    # Would be good to create a relationship with the session table here
    SessionID = Column(Integer)
    VendorID = Column(String(30))
    LocationID = Column(String(30))
    EVSEID = Column(String(30))
    PortID = Column(String(30))
    IntervalStartDateTime = Column(DateTime)
    IntervalEndDateTime = Column(DateTime)
    # For the next 3 lines, we might need to adjust the precision, depending on the wanted results
    IntervalKWH = Column(Float)
    IntervalMaxDemandKW = Column(Float)
    IntervalAverageDemandKWH = Column(Float)
    DREventCalled = Column(String(30))
    DREVentParticipated = Column(String(30))

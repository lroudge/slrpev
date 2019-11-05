#!/usr/bin/python3
"""DataSession and DataInterval models for the MySQL tables"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class DataSession(Base):
    """Class for the session data of the ev_charger"""

    __tablename__ = "session"
    SessionID = Column(String(30), primary_key=True)
    VendorID = Column(String(30))
    LocationID = Column(String(30))
    EVSEID = Column(String(30))
    PortID = Column(String(30))
    EVSEModelNbr = Column(String(30))
    EVSENbrOfPorts = Column(String(30))
    SessionStartDateTime = Column(String(30))
    SessionEndDateTime = Column(String(30))
    SessionConnectionTime = Column(String(30))
    Duration_StateC = Column(String(30))
    SessionKWH = Column(String(30))
    SessionMaxDemandKW = Column(String(30))
    SessionAverageDemandKWH = Column(String(30))
    SessionSaleAmount = Column(String(30))
    VehicleMake = Column(String(30))
    VehicleModel = Column(String(30))
    UserID = Column(String(30))
    DREventCalled = Column(String(30))
    DREventParticipated = Column(String(30))

class Interval(Base):
    """Class for the interval data of the ev_charger
    The name of the table is intentionally intervall with two l
    because the word interval was reserved in mysql"""

    __tablename__ = "intervall"
    IntervalID = Column(String(30), primary_key=True)
    SessionID = Column(String(30))
    VendorID = Column(String(30))
    LocationID = Column(String(30))
    EVSEID = Column(String(30))
    PortID = Column(String(30))
    IntervalStartDateTime = Column(String(30))
    IntervalEndDateTime = Column(String(30))
    IntervalKWH = Column(String(30))
    IntervalMaxDemandKW = Column(String(30))
    IntervalAverageDemandKWH = Column(String(30))
    DREventCalled = Column(String(30))
    DREVentParticipated = Column(String(30))

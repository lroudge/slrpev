#!/usr/bin/python3
"""Parses a csv file and puts the data in a MySQL database"""

import csv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models_csv import Base, DataSession, Interval

def parse_session():
    """Parses the session csv file and stores it into the database"""
    with open('session.csv', mode='r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/ecal_ev_charger'
                               .format(sys.argv[1], sys.argv[2],
                                       pool_pre_ping=True))
        Base.metadata.create_all(engine)
        session = Session(engine)

        line = 0
        for row in csv_reader:
            if line == 0:
                keys = row.copy()
                line += 1
            else:
                new_session = DataSession()
                for i in range(0, len(row)):
                    setattr(new_session, keys[i], row[i])
                session.add(new_session)
                session.commit()
                line += 1
        session.close()

def parse_interval():
    """Parses the interval csv file and stores it into the database"""
    with open('interval.csv', mode='r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/ecal_ev_charger'
                               .format(sys.argv[1], sys.argv[2],
                                       pool_pre_ping=True))
        Base.metadata.create_all(engine)
        session = Session(engine)

        line = 0
        for row in csv_reader:
            if line == 0:
                keys = row.copy()
                line += 1
            else:
                new_interval = Interval()
                for i in range(0, len(row)):
                    setattr(new_interval, keys[i], row[i])
                session.add(new_interval)
                session.commit()
                line += 1
        session.close()

"""This will make sure the two above functions will be called when the script is run, but not when imported"""
if __name__ == "__main__":
    parse_session()
    parse_interval()

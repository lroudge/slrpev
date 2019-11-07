#!/usr/bin/python3
"""Parses a csv file and puts the data in a MySQL database
First argument to the script is the mysql username, second is mysql password
The name of the database is ecal_ev_charger"""

import csv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models_csv import Base, DataSession, Interval

def parse_session():
    """Parses the session csv file and stores it into the database"""
    with open('session.csv', mode='r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        # Create a db engine to connect to the ecal_ev_charger db
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/ecal_ev_charger'
                               .format(sys.argv[1], sys.argv[2],
                                       pool_pre_ping=True))
        Base.metadata.create_all(engine)
        session = Session(engine)

        line = 0
        for row in csv_reader:
            if line == 0:
                # Take the first line containing the field names
                # to create a list of keys
                keys = row.copy()
                line += 1
            else:
                # Create a DataSession object with the current line of data
                # where each attribute is a field name from keys
                # and each value is the corresponding field from the current line
                new_session = DataSession()
                for i in range(0, len(row)):
                    setattr(new_session, keys[i], row[i])
                # Commit the Object as a table row to the db
                session.add(new_session)
                session.commit()
                line += 1
        session.close()

def parse_interval():
    """Parses the interval csv file and stores it into the database"""
    with open('interval.csv', mode='r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        # Create a db engine to connect to the ecal_ev_charger db
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/ecal_ev_charger'
                               .format(sys.argv[1], sys.argv[2],
                                       pool_pre_ping=True))
        Base.metadata.create_all(engine)
        session = Session(engine)

        line = 0
        for row in csv_reader:
            if line == 0:
                # Take the first line containing the field names
                # to create a list of keys
                keys = row.copy()
                line += 1
            else:
                # Create a Interval object with the current line of data
                # where each attribute is a field name from keys
                # and each value is the corresponding field from the current line
                new_interval = Interval()
                for i in range(0, len(row)):
                    setattr(new_interval, keys[i], row[i])
                # Commit the Object as a table row to the db
                session.add(new_interval)
                session.commit()
                line += 1
        session.close()

"""This will make sure the two above functions will be called when the script is run, but not when imported"""
if __name__ == "__main__":
    parse_session()
    parse_interval()

#!/usr/bin/python3
# Creates the State “California” with the City “San Francisco” from the
# database hbtn_0e_100_usa

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, psw, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cali = State(name="California")
    sf = City(name="San Francisco")
    cali.cities.append(sf)
    session.add(cali)
    session.commit()
    session.close()

#!/usr/bin/python3
# Lists all State objects, and corresponding City objects,
# contained in the database hbtn_0e_101_usa

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
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
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()

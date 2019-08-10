#!/usr/bin/python3
# Prints all City objects from the database hbtn_0e_14_usa

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, psw, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    for c, s in session.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()

#!/usr/bin/python3
# Adds the State object “Louisiana” to the database hbtn_0e_6_usa

import sys
from model_state import Base, State
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
    louisiana = State(name="Louisiana")
    states = session.query(State)
    session.add(louisiana)
    print(states.filter_by(name="Louisiana").first().id)
    session.commit()
    session.close()

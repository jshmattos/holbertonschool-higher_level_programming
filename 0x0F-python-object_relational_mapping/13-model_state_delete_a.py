#!/usr/bin/python3
# Deletes all State objects with a name containing the letter a from the
# database hbtn_0e_6_usa

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
    states = session.query(State)
    for state in states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
    session.close()

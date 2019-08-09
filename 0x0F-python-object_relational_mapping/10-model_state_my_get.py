#!/usr/bin/python3
# Prints the State object with the name passed as argument from the
# database hbtn_0e_6_usa


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, psw, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    states = session.query(State)
    found = False
    for state in states:
        if state_name == state.name:
            found = True
            print(state.id)
    if not found:
        print("Not found")
    session.close()

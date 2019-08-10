#!/usr/bin/python3

"""
This modules contains the City class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                # unique=True
                )
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False,
                      )

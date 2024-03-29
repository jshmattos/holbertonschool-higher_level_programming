#!/usr/bin/python3

"""
This modules contains the State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True
                )
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")

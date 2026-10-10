#!/usr/bin/python3

"""Module of sqlachemy"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, relationship

Base = declarative_base()


class City(Base):
    """Creates a DB"""
    __tablename__ = "cities"
    id = Column(
        Integer, primary_key=True, nullable=False,
        unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")

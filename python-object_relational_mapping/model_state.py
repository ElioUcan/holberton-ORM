#!/usr/bin/python3

"""Module of sqlachemy"""

from sqlachemy import Column, Integer, String, create_engine
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name_- == "__main__":
        engine = create_engine('mysql+mysqldb://@localhost:3306/states')
        Base.metadata.create_all(engine)

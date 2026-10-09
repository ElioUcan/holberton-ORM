#!/usr/bin/python3

"""Module of sqlachemy"""

from sqlachemy import Column, Integer, String, create_engine
from sqlachemy.ext.declarative import declarative_base
from sys import argv
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name_- == "__main__":
        passwd = argv[2]
        user = argv[1]
        engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost:3306/states')
        Base.metadata.create_all(engine)

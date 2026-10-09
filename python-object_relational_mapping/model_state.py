#!/usr/bin/python3

"""Module of sqlachemy"""

from sqlalchemy import Column, Integer, String, create_engine
from sqldblchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)

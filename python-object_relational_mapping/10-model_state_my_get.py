#!/usr/bin/python3

"""Module of sqlalchemy"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]
    engine = (
        create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id.asc())
        .first()
    )
    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")
    session.close()

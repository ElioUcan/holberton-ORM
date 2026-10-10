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
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State.name.like('%a%')).order_by(State.id.asc()).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
    session.close()

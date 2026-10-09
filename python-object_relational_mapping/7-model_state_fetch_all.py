#!/usr/bin/python3

"""Module of sqlachemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

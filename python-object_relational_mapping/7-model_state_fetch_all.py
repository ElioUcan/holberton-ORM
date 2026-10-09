#!/usr/bin/python3

"""Module of sqlachemy"""
from sqlachemy import create_engine
from model_state import import Base, State
from sys import argv

Base = declarative_base()
if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")
    with engine.connect() as conn:
        query = conn.execute(text("SELECT * FROM states ORDER BY id ASC"))
        for row in query:
            print(row.id, row.name)

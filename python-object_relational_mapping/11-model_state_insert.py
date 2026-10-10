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
    nuevo_producto = Product(name=state_name)
    session.add(nuevo_producto)
    session.commit()
    print(f"{nuevo_producto.id}")
    session.close()

#!/usr/bin/python3

"""Prints all elements of City"""

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    host = "localhost"
    port = 3306

    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(State, City)
    .filter(State.id == City.state_id)
    .order_by(City.id.asc())
    .all()
    )
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()

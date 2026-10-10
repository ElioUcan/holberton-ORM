#!/usr/bin/python3

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

    results  = session.query(City).order_by(City.id)
    session.close()

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc()).first()
    if states == None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
    session.close()

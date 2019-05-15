# Author: Ali Azhari


from sqlalchemy import create_engine

# create_engine connects to the database
# The echo flag is a shortcut to setting up SQLAlchemy logging,
# which is accomplished via Python’s standard logging module.
# it is set to true, all the generated SQL produced will be printed out

from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("mysql://user:passwrd@localhost/chat_db",echo = True)

# session might be irrelevant in this example, but imagine you have multiple users using the database at the same time,
# session manages to keep track of each user

db = scoped_session(sessionmaker(bind=engine))

def main():
    agents = db.execute("SELECT lastname, firstname, password FROM agents").fetchall()
    for agent in agents:
        print(f"{agent.lastname}, {agent.firstname}, {agent.password}")

if __name__ == "__main__":
    main()


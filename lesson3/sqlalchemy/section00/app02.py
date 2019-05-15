# Author: Ali Azhari

# Using multiple SQL commands.

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql://ali:ali@localhost/chat_db", echo=False)
db = scoped_session(sessionmaker(bind=engine))

def main():

    # List all flights.
    agents = db.execute("SELECT id, lastname, firstname, name FROM agents").fetchall()
    for agent in agents:
        print(f"agent {agent.id}, {agent.lastname},  {agent.firstname}, {agent.name}.")

    # Prompt user to choose a agent.
    agent_id = int(input("\nAgent ID: "))
    agent = db.execute("SELECT lastname, firstname, name FROM agents WHERE id = :id",
                        {"id": agent_id}).fetchone()

    # Make sure flight is valid.
    if agent is None:
        print("Error: No such agent.")
        return

    # List chats.
    chats = db.execute("SELECT customer_id, dt FROM chats WHERE agent_id = :agent_id",
                            {"agent_id": agent_id}).fetchall()
    print("\nChats:")
    for chat in chats:
        print(chat.customer_id, chat.dt)
    if len(chats) == 0:
        print("No chats.")

if __name__ == "__main__":
    main()
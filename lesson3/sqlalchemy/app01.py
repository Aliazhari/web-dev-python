# Author: Ali Azhari

# importing an csv file to mysql

import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql://ali:ali@localhost/chat_db", echo=False)
db = scoped_session(sessionmaker(bind=engine))


def main():
    csv.register_dialect('myCustomers', delimiter=',', skipinitialspace=True)
    f = open('customers.csv')
    reader = csv.reader(f, 'myCustomers')
    for name, ip, subject in reader:
        db.execute("INSERT INTO customers (name, ip, subject) VALUES (:name, :ip, :subject)",
                   {"name": name, "ip": ip, "subject": subject})
        print(f"Added customer  {name} with ip  {ip} and subject: {subject}.")
    db.commit()


if __name__ == "__main__":
    main()

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+mysqldb://root:ali1025@localhost/school_db")

db = scoped_session(sessionmaker(bind=engine))


def main():
    classes = db.execute("Select name, lastname, room, section, year, type from classes JOIN courses ON "
                         "classes.course_id = courses.id JOIN staff ON classes.staff_id = staff.id").fetchall()
    for aClass in classes:
        print(f"{aClass.name} {aClass.lastname} {aClass.room} {aClass.section}")


if __name__ == "__main__":
    main()

duhhhhh
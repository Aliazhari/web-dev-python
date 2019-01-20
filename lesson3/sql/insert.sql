# Inserting students in table students

INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Smith', 'John', 'john@smith.com', 22, '111111111');
INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Milky', 'Robert', 'robert@milky.com', 23, '222222222');
INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Birm', 'Susan', 'susan@Birm.com', 21, '333333333');
INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Mooney', 'Debra', 'debra@mooney.com', 24, '444444444');
INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Adel', 'Ali', 'ali@adel.com', 20, '555555555');
INSERT INTO students ( lastname, firstname, email, age, ssn) VALUES ('Gonzales', 'Mary', 'maryn@gonzales.com', 22, '666666666');

# Inserting courses  in table courses

INSERT INTO courses ( name, number, description) VALUES ('Python', 'CS120', 'A web development with Python and Javascript. This courses covers SQL, Git and many other technologies');
INSERT INTO courses ( name, number, description) VALUES ('Introduction to Java', 'CS130', 'An Introduction to Java. Covers data types, conditions, loop and classes');
INSERT INTO courses ( name, number, description) VALUES ('Data structures', 'CS250', 'First half of the term covers Data structures: Arrays, Linklist, Verctors, HashMap, Hashtable..etc');
INSERT INTO courses ( name, number, description) VALUES ('Modern History', 'HIS320', 'An Introduction to mocern history. Covers world war I and II');
INSERT INTO courses ( name, number, description) VALUES ('Introduction to Psychology', 'PSY101', 'An introduction to Psychology');
INSERT INTO courses ( name, number, description) VALUES ('Calculus I', 'MATh271', 'Introduction to calculus. Covers derivitives and integrals');

# Inserting staff in table staff

INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Kerry', 'Chad', 'chad@kerry.com', 42, '111111110');
INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Devall', 'Christine', 'christine@devall.com', 43, '222222221');
INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Obrien', 'Brian', 'brian@obrien.com', 51, '333333332');
INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Clinton', 'Lisa', 'lisa@clinton.com', 64, '444444443');
INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Ben', 'Mohamed', 'mohamed@ben.com', 50, '555555554');
INSERT INTO staff ( lastname, firstname, email, age, ssn) VALUES ('Franklin', 'Jasmine', 'jasmine@franklin.com', 42, '666666665');

#Inserting classes in table classes

INSERT INTO classes ( course_id, staff_id, room, section, year,type ) VALUES (2, 3, 101, 1, 2019, 'Spring');
INSERT INTO classes ( course_id, staff_id, room, section, year, type) VALUES (3, 3, 102, 1, 2019, 'Spring');
INSERT INTO classes ( course_id, staff_id, room, section, year, type) VALUES (4, 4, 103, 1, 2019, 'Spring');
INSERT INTO classes ( course_id, staff_id, room, section, year, type) VALUES (4, 6, 104, 2, 2019, 'Spring');
INSERT INTO classes ( course_id, staff_id, room, section, year, type) VALUES (5, 1, 105, 1, 2019, 'Spring');
INSERT INTO classes ( course_id, staff_id, room, section, year, type) VALUES (1, 2, 106, 1, 2019, 'Spring');

#Inserting students in table enrollment

INSERT INTO enrollment ( student_id, class_id ) VALUES (1, 1);
INSERT INTO enrollment ( student_id, class_id) VALUES (2, 1);
INSERT INTO enrollment ( student_id, class_id) VALUES (3, 1);
INSERT INTO enrollment ( student_id, class_id) VALUES (4, 3);
INSERT INTO enrollment ( student_id, class_id) VALUES (5, 3);
INSERT INTO enrollment ( student_id, class_id) VALUES (6, 3);

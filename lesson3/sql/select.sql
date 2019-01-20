SELECT * FROM students;
SELECT lastname FROM students;
SELECT firstname, lastname FROM students;
SELECT age FROM students;
SELECT * FROM STUDENTS WHERE ID = 3;
SELECT * FROM STUDENTS WHERE ID > 3;
SELECT * FROM STUDENTS WHERE ID > 3 AND id < 6;
SELECT * FROM STUDENTS WHERE lastname = 'Smith';
SELECT AVG(age) FROM students;
SELECT COUNT(*) FROM  students;
SELECT COUNT(*) FROM  students WHERE age > 22;
SELECT MIN(age)  FROM students;
SELECT MAX(age)  FROM students;
SELECT * FROM students WHERE lastname LIKE '%S%';
SELECT  DISTINCT age, lastname FROM students;
SELECT * FROM STUDENTS WHERE lastname = 'Smith' OR age = 23;
SELECT COUNT(*) FROM (SELECT DISTINCT age FROM students)  AS DistinctAges;
SELECT * FROM students LIMIT 2;
SELECT * FROM students ORDER BY  lastname ASC;

Select name, staff_id, room, section, year, type from classes JOIN courses ON classes.course_id = courses.id;

Select name, lastname as Instructor_Lastname, firstname as Instructor_Firstname, room, section, year, type from classes JOIN courses ON classes.course_id = courses.id JOIN staff ON classes.staff_id = staff.id;


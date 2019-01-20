#Alter the classes table

ALTER TABLE classes ADD FOREIGN KEY (course_id) REFERENCES Courses(id);
ALTER TABLE classes ADD FOREIGN KEY (staff_id) REFERENCES staff(id);

# alter the enrollment table

ALTER TABLE enrollment ADD FOREIGN KEY (student_id) REFERENCES students(id);
ALTER TABLE enrollment ADD FOREIGN KEY (class_id) REFERENCES classes(id);


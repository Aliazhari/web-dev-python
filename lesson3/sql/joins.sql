SELECT name, number, room FROM `classes` INNER JOIN `courses` ON courses.id = classes.course_id
SELECT name, number, room FROM `classes` JOIN `courses` ON courses.id = classes.course_id;
SELECT name, number, room FROM `classes` LEFT OUTER JOIN `courses` ON courses.id = classes.course_id;
SELECT name, number, roomm FROM `classes` RIGHT OUTER JOIN `courses` ON courses.id = classes.course_id;

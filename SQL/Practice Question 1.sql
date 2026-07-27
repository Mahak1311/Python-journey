CREATE DATABASE IF NOT EXISTS college;

USE college;

CREATE TABLE teachers(
id INT PRIMARY KEY,
name VARCHAR(30),
subject VARCHAR(30),
salary INT
);
INSERT INTO teachers
VALUES
(23,"Ajay","Maths",50000),
(47,"Bharat","English",60000),
(18,"Chetan","Chemistry",45000),
(9,"Divy","Physics",70000);

SELECT * FROM teachers;

SELECT * FROM teachers
WHERE salary>55000;

ALTER TABLE teachers
CHANGE COLUMN salary ctc INT;

SELECT * FROM teachers;

UPDATE teachers
SET ctc = ctc + ctc*0.25;

SELECT * FROM teachers;

ALTER TABLE teachers
ADD COLUMN city VARCHAR(30) DEFAULT "Gurgaon";

ALTER TABLE teachers
DROP COLUMN ctc;

SELECT * FROM teachers;






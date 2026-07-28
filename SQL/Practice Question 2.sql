USE college;

CREATE TABLE student(
 rollno  INT PRIMARY KEY,
 name VARCHAR(30),
 city VARCHAR(30),
 marks INT
 );
 
 INSERT INTO student
 (rollno,name,city,marks)
 VALUES
 (110,"adam","Delhi",76),
 (108,"bob","Mumbai",65),
 (124,"cassey","Pune",94),
 (112,"Duke","Pune",80);
 
 SELECT * FROM student;
 
 SELECT * FROM student
 WHERE marks>75;
 
 SELECT name,city from student;
 
 SELECT city , MAX(marks)
 FROM student
 GROUP BY city;

SELECT avg(marks)
FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(2);

UPDATE student
SET grade="O"
WHERE marks>=80;

UPDATE student
SET grade="A"
WHERE marks>=70 AND marks < 80;

UPDATE student
SET grade="B"
WHERE marks>=60 AND marks < 70;

SELECT * FROM student;
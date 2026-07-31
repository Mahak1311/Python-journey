CREATE DATABASE Employee;

USE Employee;

CREATE TABLE employee(
empid INT,
firstname VARCHAR(30),
lastname VARCHAR(30),
department VARCHAR(30),
salary INT,
hiredate DATE
);
INSERT INTO employee
(empid,firstname,lastname,department,salary,hiredate)
VALUES
(101,"Alice","Johnson","IT",6500, '2020-03-15'),
(102,"Mark","Rivera","HR",4800,'2019-07-22'),
(103,"Sophia","Lee","Finance",7200,'2021-01-10'),
(104,"Daniel","Kim","IT",5800,'2018-11-05'),
(105,"Emma","Brown","Marketing",5300,'2022-04-18'),
(106,"Liam","Patel","Finance",6900,'2020-09-29'),
(107,"Olivia","Garcia","HR",4600,'2017-06-30'),
(108,"Noah","Thompson","IT",7500,'2023-02-12'),
(109,"Ava","Martinez","Marketing",5100,'2019-12-12'),
(110,"Ethan","Davis","Finance",8000,'2016-05-14');

SELECT * FROM employee;

SELECT firstname,lastname,salary FROM employee;

SELECT * FROM employee
WHERE department="IT";

SELECT * FROM employee
WHERE salary>6000;

SELECT * FROM employee
ORDER BY hiredate DESC;

SELECT DISTINCT department FROM employee;

/* To print info where first name starts with A and for ends with use "%a" and many more LIKE function */
SELECT * FROM employee
WHERE firstname LIKE "A%";

SELECT * FROM employee
WHERE salary>4000 AND salary<7000;

SELECT department,AVG(salary) FROM employee
GROUP BY department;

SELECT department,count(*) FROM employee
GROUP BY department
HAVING count(*)>2;

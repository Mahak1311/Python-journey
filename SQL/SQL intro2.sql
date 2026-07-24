CREATE DATABASE user;
USE user;

CREATE TABLE user(
id INT ,
age INT ,
name VARCHAR(30) NOT NULL,
email VARCHAR(30) UNIQUE,
followers INT DEFAULT 0,
following INT,
CONSTRAINT CHECK (age>= 13),
PRIMARY KEY (id)
);

INSERT INTO user
(id,age,name,email)
VALUES
(1,16,"adam","adam@yahoo.in");

DELETE FROM user
WHERE id=1;

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(101,19,"adam","adam@yahoo.in",115,26),
(102,17,"cassey","cass@gmail.com",1150,1),
(103,14,"bob","bobby@gmail.com",29,29),
(104,24,"tony","tones@email.com",3000,4),
(105,22,"peter","peterparker@yahoo.in",360,19);

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(106,19,"eve","eve@yahoo.in",1345,206),
(107,24,"pepper","salt@gmail.com",1,32),
(108,21,"mj","gf@yahoo.in",11,6);

INSERT INTO user
(id,age,name,email,following)
VALUES
(109,19,"karen","spongebob@yahoo.in",206);


INSERT INTO user
(id,age,name,email,following)
VALUES
(110,19,"karenn","spongebobb@yahoo.in",206);

SELECT *
FROM user
WHERE followers>=200;

CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(30),
user_id INT,
FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO post
(id,content,user_id)
VALUES
(201,"HELLO WORLD",102),
(202,"I am backk",105),
(203,"Bye Bye",101);

SELECT * FROM post;

SELECT age,followers FROM user;

 -- AND is used to check if both condition is true
SELECT name,age,followers
FROM user
WHERE age>14 AND followers>200; 

-- OR is used to check for one condition to be true 
SELECT name,age,followers
FROM user
WHERE age>16 OR following>100; 

-- BETWEEN is used to select between given range
SELECT name,age,followers
FROM user
WHERE age BETWEEN 15 AND 17;

-- IN is used to match values in given condition 
SELECT name,age,followers
FROM user
WHERE email IN ("peterparker@yahoo.in","adam@yahoo.in","tones@email.com","mahak@gmail.com");

SELECT name,age,followers
FROM user
WHERE age IN (14,16);

-- NOT is used to negate given condition
SELECT name,age,followers
FROM user
WHERE age NOT IN (17,22);

-- LIMIT clause sets an upper limit on number of tuples to be returned
SELECT name,age,followers,following
FROM user
WHERE age>10 
LIMIT 2;

SELECT id,name,age,followers,following
FROM user
LIMIT 3;

-- ORDER BY clause is used to sort in ascending or in descending order
SELECT name,age
FROM user
ORDER BY age ASC;

SELECT name,followers
FROM user
ORDER BY followers DESC;

/* aggregate functions- to perform cal and return single value
COUNT()- to count appearances
MAX()- to find maximumm
MIN()- to find minimum
SUM()- to find the sum
AVG()- to find the average*/

SELECT COUNT(age)
FROM user
WHERE age>20;

SELECT MAX(followers)
FROM user;

SELECT MIN(following)
FROM user;

SELECT SUM(followers)
FROM user;

SELECT AVG(age)
FROM user;

-- GROUP BY 
SELECT age, COUNT(age)
FROM user
GROUP BY age;

SELECT age,MAX(followers)
FROM user
GROUP BY age;

-- HAVING CLAUSE works like WHERE clause but for groups
SELECT age,MAX(followers)
FROM user
GROUP BY age
HAVING MAX(followers)>370;

-- Table queries

UPDATE user
SET following=100
WHERE age=19;

SET SQL_SAFE_UPDATES=0;

SELECT * FROM user;

 DELETE FROM user
 WHERE age=14;
 
 SELECT * FROM user;
 
 -- ALTER QUERIES
 
 ALTER TABLE user 
 ADD COLUMN city VARCHAR(50) DEFAULT "Delhi";
 
 SELECT * FROM user;
 
ALTER TABLE user
DROP COLUMN city;

SELECT * FROM user;
 
ALTER TABLE user
RENAME TO instauser;

SELECT * FROM instauser;  
  
ALTER TABLE instauser
RENAME TO user;
 
ALTER TABLE user
CHANGE COLUMN followers subs INT DEFAULT 0; 

SELECT * FROM user;
   
ALTER TABLE user
MODIFY subs INT DEFAULT 5;

SELECT * FROM user;
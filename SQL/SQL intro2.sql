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

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(101,19,"adam","adam@yahoo.in",115,26),
(102,17,"cassey","cass@gmail.com",1150,1),
(103,14,"bob","bobby@gmail.com",29,29),
(104,24,"tony","tones@email.com",3000,4),
(105,22,"peter","peterparker@yahoo.in",360,19);

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
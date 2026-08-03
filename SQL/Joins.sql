CREATE DATABASE joins;

USE joins;

CREATE TABLE customers(
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers
(customer_id,name,city)
VALUES
(1,"Alice","Mumbai"),
(2,"Bob","Delhi"),
(3,"Charlie","Bangalore"),
(4,"David","Mumbai");

CREATE TABLE orders(
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders
(order_id,customer_id,amount)
VALUES
(101,1,500),
(102,1,900),
(103,2,300),
(104,5,700);

SELECT * FROM customers;
SELECT * FROM orders;

-- Inner Join

SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

-- left join- takes all of left table and only matching values from right table
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id;

-- right join- takes all of right table and matching values from left table only

SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id=o.customer_id;

-- Outer join- Union of left join and right join
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id=o.customer_id;

-- Cross join- matches every data of table a to every data of table b
SELECT *
FROM customers
CROSS JOIN orders;

-- Self join- kinda like inner join,works like regular join on same table
SELECT *
FROM customers as A
JOIN customers as B
ON A.customer_id=B.customer_id;
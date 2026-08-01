CREATE DATABASE transactions;

USE transactions;

CREATE TABLE accounts(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(30),
balance int
);

INSERT INTO accounts
(name,balance)
VALUES
("Adam",500.00),
("Bob",300.00),
("Charlie",1000.00);

SELECT * FROM accounts;

START TRANSACTION;

-- to debit
UPDATE accounts
SET balance=balance-50
WHERE id=1;

-- to credit
UPDATE accounts
SET balance=balance+50
WHERE id=2;

COMMIT;

START TRANSACTION;

UPDATE accounts
SET balance=balance+100
WHERE id=1;

COMMIT;

-- here autocommit is on so it got auto commited and couldn't get rollback-ed
UPDATE accounts
SET balance=balance+500
WHERE id=2;

-- to check if autocommit is on or off
SELECT @@autocommit;

-- It undo's statements which are not commited only
ROLLBACK;

-- SAVEPOINT

START TRANSACTION;

UPDATE accounts
SET balance=balance+1000
WHERE id=1;

SAVEPOINT after_wallet_topup;

UPDATE accounts
SET balance=balance+10
WHERE id=1;

-- if an error occurs and we need to undo a statement but not the whole transaction we use "rollback to"
ROLLBACK TO after_wallet_topup;

COMMIT;




 
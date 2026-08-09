CREATE DATABASE others;
USE others;

CREATE TABLE accounts(
account_id INT PRIMARY KEY,
name VARCHAR(20),
balance INT,
branch VARCHAR(30)
);

INSERT INTO accounts 
(account_id,name,balance,branch)
VALUES
(1,"Adam",500.00,"Mumbai"),
(2,"Bob",1000.00,"Delhi"),
(3,"Kelly",15000.00,"Bangalore"),
(4,"Ken",200.00,"Ahmedabad");

SELECT * FROM accounts;

CREATE INDEX id_branch ON accounts(branch);

SHOW INDEX FROM accounts;

CREATE INDEX id_2 ON accounts(balance,branch);

DROP INDEX id_2 ON accounts;

DELIMITER //

CREATE PROCEDURE check_balance(IN  acc_id INT, OUT bal DECIMAL(10,2))
BEGIN
  SELECT balance
  FROM accounts
  WHERE account_id=acc_id;
END //  

DELIMITER ;

CALL check_balance(2, @balance);
SELECT @balance;





  
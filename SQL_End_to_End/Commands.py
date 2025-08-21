# Q1. What is DDL in SQL? Give examples.
# A:
# DDL stands for Data Definition Language. These statements define, modify, or remove the structure of database objects (like tables, views, indexes).
# Examples: CREATE, ALTER, DROP, TRUNCATE, RENAME.
#
# Q3. How does ALTER work? Give an example.
# A:
# ALTER modifies an existing database object without deleting it.
#Add a new column
# ALTER_TABLE employees ADD date_of_joining DATE;

# #Modify column datatype
# ALTER TABLE employees MODIFY salary DECIMAL(10,2);
#
# #Rename
# ALTER TABLE employees RENAME COLUMN name TO emp_name

# Q4. How to rename a table in SQL?
# RENAME TABLE old_table_name TO new_table_name;

# Q5. What is DML in SQL? Give examples.
# DML means data manipulation language
# INSERT,UPDATE,DELETE
# They are transactional (changes can be rolled back)

# Q6. How do you insert multiple rows in a single query?
#
# INSERT INTO employees (name,department,salary) VALUES
# ('john','IT',40000),
# ('max','IT',50000),
# ('Jack','it',80000);

# Q7. What is the difference between UPDATE and INSERT ON DUPLICATE KEY UPDATE?
# UPDATE modifies existing rows based on condition
# INSERT ON DUPLICATE KEY UPDATE inserts new data but updates it if a duplicate primary key exists
#
# INSERT INTO employees (id, name, salary)
# VALUES (1, 'John', 55000)
# ON DUPLICATE KEY UPDATE salary = 55000;

# Q8. What is DQL in SQL?
# Data Query language it is used to retrieve data from a database
# Main command is SELECT

# Q9. Difference between WHERE and HAVING clauses?
# WHERE = Filtering rows before grouping and works with columns
# HAVING = Filtering after grouping and works with Aggregate functions

# SELECT department, COUNT(*) AS emp_count
# FROM employees
# GROUP BY department
# HAVING COUNT(*) >5;

# Q10. How to fetch the top 5 highest salaries?
# SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

# Q11. What is DCL in SQL?
# DCL stands data control language it controls database access privileges
# Ex: GRANT,REVOKE

# Q12. Difference between GRANT and REVOKE?
# GRANT = Gives privileges to users
# REVOKE = Removes privileges

# GRANT SELECT, INSERT ON employees TO 'user1'@'localhost';
#
# REVOKE INSERT ON employees FROM 'users1'@'localhost';

# Q13. What is TCL in SQL?
# TCL Stands for Transaction control language it manages transactions within a database
# EX: COMMIT,ROLLBACK,SAVEPOINT,SET TRANSACTION

# Q14. Explain COMMIT and ROLLBACK with an example.
#
# BEGIN;
# -- Start
# transaction
#
# UPDATE
# employees
# SET
# salary = salary + 5000
# WHERE
# department = 'IT';
#
# -- If
# correct
# COMMIT;
#
# -- If
# wrong
# ROLLBACK;
# Commit = Saves changes permanently
# Rollback = Reverts changes to the last commit or savepoint

# Q15. What is a SAVEPOINT?
# A savepoint is a check point within a transaction to which you can rollback without affecting the entire transaction
#
# BEGIN;
#
# UPDATE employees SET salary = 50000 WHERE id = 1;
# SAVEPOINT sp1;
#
# UPDATE employees SET salary = 60000 WHERE id = 2;
# ROLLBACK TO sp1; -- Undo only the second update
#
# COMMIT;




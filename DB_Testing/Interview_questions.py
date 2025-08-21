# 1. What is Database Testing?
# DB testing involves validating the schema, tables,triggers stored procedures and data integrity in the
# backend database to ensure the data is consistent and correctly stored as per business rules

# 2. What are the types of Database Testing?
# Structural Testing = (Schema,table format,columns)
# Data validity Testing = (Correctness of data)
# Data Integrity testing = (relations b/w tables)
# Stored Procedures/Functions Testing
# Performance Testing(queries,indexing)
#
# 3. What do you verify in DB testing?
# Data is inserted/updated/deleted correctly
# No data loss or truncation
# Referential integrity b/w tables
# Triggers and stored procedures are firing as expected
#
# 4. What tools are used for DB Testing?
# Manual = DBeaver,SQL Developer
# Automation = Python
#
# 5. What is a Primary Key and Foreign Key?
# Primary key = Uniquely identifies each record in a table
# Foreign key = Links one table to another and maintain  referential integrity

# 6. How do you validate data in the database from UI?
# Submit a form via UI,then connects to the DB  and run a SQL SELECT query to validate if the data was correctly
# (inserted)

# 7. What is Data Integrity?
# It ensures data is accurate and consistent across all
# (relationships)

# 8. How do you perform backend testing in automation?
# Use java or python to connect to the database,execute SQL queries and insert the returned results against expected values
#
# 9. What are stored procedures and how do you test them?
# Stored procedures are precompiled SQL Code they are tested by executing them with sample input and checking the output or affected tables
#
# 10.What are common issues found in DB Testing?
# Data mismatch
# Null or incorrect values
# Constraint violations
# Broken joins/relationships
# SQL injection vulnerabilities
#
# 11. Write a query to find duplicate records in a table.
# SELECT name COUNT(*)
# FROM employees
# GROUP BY name
# HAVING COUNT(*)>1;

# 12. How do you test for referential integrity?
# check that:
#     Foreign  key values exist in the parent table
#     deleting a parent does not orphan child records
#
# 13. Can you automate database testing?
# yes using:
#     Python : pyodbc
#     Integration with selenium, API tests or jenkins
#
# 14. How to verify stored procedure logic?
# call the procedure with known input
# Query affected tables
# validate outputs, updates and return messages

# 15. How to test triggers in a table?
# Perform insert/update/delete actions that fire the trigger.
# Check the action taken by the trigger (like audit log entries or updates).

# 17. How do you handle NULL values in testing?
# SELECT * FROM users WHERE address IS NULL;

# 18. How do you test a function that returns a table?
# call the function SELECT * FROM function_name(params) and validate the return rows

# 19. What is a JOIN and how do you test it?
# JOIN combines rows from multiple tables based on related columns

# 20. How do you test performance of a SQL query?
# Use EXPLAIN PLAN, Analyze, or Execution plan
# check for slow joins, missing indexes or large scans










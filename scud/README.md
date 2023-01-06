Note: This utility is currently more suitable to be used in a notebook settings, as it will prompt user for input. A Version more fir to be used in programming will soon be released.

I was recently doing an online training, the instructor was showing examples on MySQL database. I however preferred running those exampkes on my test database i.e. MS SQL Server on Azure Cloud. 

After a few classes i realized that MYSQL has host of simple to understand SQL queries, where as its SQL server equivalent was big chunky queries.
(I am talking about system SQL query which you run against the metdata such as SHOW TABLES, SHOW DATABASE etc)

with this idea i have created this utility to provide syntax to some imp queries, which we are required to run every now and then.

run [print(scup.sqlserver('list'))] to see a complete list queries, this utility support.

version = "0.4.4" -->  Added Query 9, and added header to all queries

version = "0.4.3" --> Added header to #3 and #6 query , # more details 

version = "0.4.2" --> Bug - List command but erroring - local variable 'ssquery' referenced before assignment

version = "0.4.1" --> fixed a small bug, nevermind :)

version = "0.4.0" --> Added option to call queries by numbers

version = "0.3.0" --> Changed scup.py function ms2ssf() name to sqlserver(). added many other sqls.

version = "0.2.3" --> Package Name changed from MSS to SCUP as pypi showed conflict. (SCUP as in SQL Covertor Utility Program)

version = "0.2.2" --> List command added and reponse to no query match added

version = "0.2.0" --> 3 Show commands working

version = "0.2.1" --> Patch - test scripts was commented out

--------------------------------------------------------------------------------------------------

COMMANDS HELP  ()

        1. SHOW DATABASES (conn.execute(scup.sqlserver('SHOW DATABASES')).fetchall())
        2. SHOW TABLES : will prompt for Schema name
        3. SHOW TABLES FROM database_name : will prompt for Database name
        4. SHOW CHECK_CONSTRAINTS FROM TABLE : will prompt for Table Name (uses LIKE)
        5. DESCRIBE TABLE  : will prompt for Database name
        6. SHOW INDEX FROM TABLE  : will prompt for Schema and Table name
        7. DATABASE STATUS  : will prompt for Database name 
        8. SHOW VIEWS : will prompt for Schema name
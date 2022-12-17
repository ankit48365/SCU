
# SHOW TABLES;  will give list alone
# SHOW FULL TABLES; will provide table type also like base table or view
# SHOW TABLES FROM database_name;



#mysql to ms sql server function
def sqlserver(msquery):

    if msquery == 'SHOW DATABASES':
        ssquery ='SELECT name FROM sys.databases;'
        # return ssquery
    elif msquery == 'SHOW TABLES':
        print("Please notice the prompt looking for input")
        SchemaName = input("Provide Schema name : ")
        ssquery = ("SELECT table_schema, table_name, table_type FROM information_schema.tables where table_schema = '"+SchemaName+"';")
    
    elif msquery == 'SHOW TABLES FROM DATABASE_NAME':
        print("Please notice the prompt looking for input")
        dbname = input("Provide Database name : ")
        ssquery = ("SELECT Table_Catalog, table_schema, table_name, table_type FROM information_schema.tables where Table_Catalog = '"+dbname+"';")

    elif msquery == 'SHOW CHECK_CONSTRAINTS FROM TABLE':
        print("Please notice the prompt looking for input")
        TblName = input("Provide Table name : ")
        ssquery = ("select con.[name] as constraint_name,schema_name(t.schema_id) + '.' + t.[name]  as [table],col.[name] as column_name,con.[definition],case when con.is_disabled = 0 then 'Active' else 'Disabled' end as [status] from sys.check_constraints con left outer join sys.objects t on con.parent_object_id = t.object_id left outer join sys.all_columns col on con.parent_column_id = col.column_id and con.parent_object_id = col.object_id where t.[name] like '%"+TblName+"%' order by con.name;")
  
    elif msquery == 'DESCRIBE TABLE':
        print("Please notice the prompt looking for input")
        TblName2 = input("Provide Table name : ")
        ssquery = ("select schema_name(tab.schema_id) as schema_name,tab.name as table_name, col.column_id,col.name as column_name, t.name as data_type, col.max_length, col.precision from sys.tables as tab inner join sys.columns as col on tab.object_id = col.object_id left join sys.types as t on col.user_type_id = t.user_type_id where tab.name like '%"+TblName2+"%' order by schema_name,table_name, column_id;")

    elif msquery == 'SHOW INDEX FROM TABLE':
        print("Please notice the prompt looking for input")
        Schemaname3 = input("Provide Schema name : ")
        TblName3 = input("Provide Table name : ")
        ssquery = ("EXEC sp_helpindex '"+Schemaname3+"."+TblName3+"'")

    elif msquery == 'DATABASE STATUS':
        print("Please notice the prompt looking for input")
        dbname4 = input("Provide Database Name : ")
        ssquery = ("SELECT status as status_id,                CASE                 WHEN status = 1 THEN 'New'                WHEN status = 2 THEN '2 not sure'                 WHEN status = 4 THEN 'select into/bulkcopy'                 WHEN status = 8 THEN 'trunc. log on chkpt'                 WHEN status = 16 THEN 'torn page detection'                WHEN status = 32 THEN 'loading'                 WHEN status = 64 THEN 'pre recovery'                WHEN status = 128 THEN 'recovering'                 WHEN status = 256 THEN 'not recovered'                WHEN status = 512 THEN 'offline'                 WHEN status = 1024 THEN 'read only'                 WHEN status = 2048 THEN 'dbo use only'               WHEN status = 4096 THEN 'single user'                 WHEN status = 8192 THEN '8192 not sure'                 WHEN status = 16384 THEN '16384 not sure'                 WHEN status = 32768 THEN 'emergency mode'                 WHEN status = 65536 THEN 'online'                 WHEN status = 131072 THEN '131072 not sure'                 WHEN status = 262144 THEN '262144 not sure'                 WHEN status = 524288 THEN '524288 not sure'                 WHEN status = 1048576 THEN '1048576 not sure'                 WHEN status = 2097152 THEN '2097152 not sure'                 WHEN status = 4194304 THEN 'autoshrink'                 WHEN status = 1073741824 THEN 'cleanly shutdown'                 ELSE 'None Provided' END AS 'Status_Values'            FROM sys.sysdatabases WHERE name = '"+dbname4+"'") 


    elif msquery == 'list':
        list1 = ("""
        1. SHOW DATABASES
        2. SHOW TABLES : will prompt for Schema name
        3. SHOW TABLES FROM database_name : will prompt for Database name
        4. SHOW CHECK_CONSTRAINTS FROM TABLE : will prompt for Table Name (uses LIKE)
        5. DESCRIBE TABLE  : will prompt for Database name
        6. SHOW INDEX FROM TABLE  : will prompt for Schema and Table name
        7. DATABASE STATUS  : will prompt for Database name """)
        print(list1)
        
    else:
        ssquery = ("SELECT distinct('NO MATCH FOR INPUT QUERY - RUN LIST FOR HELP') FROM sys.databases")


    return ssquery
   
    


# x = input('command input  ')
# print('you entered - ',x)
# h = sqlserver(x)
# print(h)
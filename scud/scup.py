
__version__ = '0.4.5'

# Important MS SQL Server Queries
def sqlserver(msquery):

# 1
    if msquery == 'SHOW DATABASES':
        ssquery ="WITH myquery02 (name) AS (select 'name' from sys.indexes union SELECT name FROM sys.databases) select * from myquery02 order by (CASE WHEN name= 'name' Then 0 else 1 end), name"
    elif msquery == '1':
        ssquery ="WITH myquery02 (name) AS (select 'name' from sys.indexes union SELECT name FROM sys.databases) select * from myquery02 order by (CASE WHEN name= 'name' Then 0 else 1 end), name"
# 2
    elif msquery == 'SHOW TABLES':
        print("Please notice the prompt looking for input")
        SchemaName = input("Provide Schema name : ")
        ssquery = ("DECLARE @table_schema varchar (30); SET @table_schema = 'dbo' ; WITH query03 (table_schema, table_name, table_type) as (select 'table_schema', 'table_name', 'table_type' from sys.indexes union SELECT table_schema, table_name, table_type FROM information_schema.tables where table_schema = @table_schema ) select * from query03 order by 2 DESC ")
    elif msquery == '2':
        print("Please notice the prompt looking for input")
        SchemaName = input("Provide Schema name : ")
        ssquery = ("DECLARE @table_schema varchar (30); SET @table_schema = 'dbo' ; WITH query03 (table_schema, table_name, table_type) as (select 'table_schema', 'table_name', 'table_type' from sys.indexes union SELECT table_schema, table_name, table_type FROM information_schema.tables where table_schema = @table_schema ) select * from query03 order by 2 DESC ")

# 3 
    elif msquery == 'SHOW TABLES FROM DATABASE_NAME':
        print("Please notice the prompt looking for input")
        dbname = input("Provide Database name : ")
        ssquery = ("DECLARE @DB_NAME VARCHAR (30);SET @DB_NAME = '"+dbname+"';WITH myquery_3 (Table_Catalog, Table_schema, Table_name, Table_type) AS (select 'Table_Catalog', 'Table_schema', 'Table_name', 'Table_type' from sys.indexes union SELECT Table_Catalog, Table_schema, Table_name, Table_type FROM information_schema.tables where Table_Catalog = @DB_NAME ) select * from myquery_3 ORDER BY 2 DESC")
    elif msquery == '3':
        print("Please notice the prompt looking for input")
        dbname = input("Provide Database name : ")
        ssquery = ("DECLARE @DB_NAME VARCHAR (30);SET @DB_NAME = '"+dbname+"';WITH myquery_3 (Table_Catalog, Table_schema, Table_name, Table_type) AS (select 'Table_Catalog', 'Table_schema', 'Table_name', 'Table_type' from sys.indexes union SELECT Table_Catalog, Table_schema, Table_name, Table_type FROM information_schema.tables where Table_Catalog = @DB_NAME ) select * from myquery_3 ORDER BY 2 DESC")

# 4
    elif msquery == 'SHOW CHECK_CONSTRAINTS FROM TABLE':
        print("Please notice the prompt looking for input")
        TblName = input("Provide Table name : ")
        ssquery = ("select con.[name] as constraint_name,schema_name(t.schema_id) + '.' + t.[name]  as [table],col.[name] as column_name,con.[definition],case when con.is_disabled = 0 then 'Active' else 'Disabled' end as [status] from sys.check_constraints con left outer join sys.objects t on con.parent_object_id = t.object_id left outer join sys.all_columns col on con.parent_column_id = col.column_id and con.parent_object_id = col.object_id where t.[name] like '%"+TblName+"%' order by con.name;")
    elif msquery == '4':
        print("Please notice the prompt looking for input")
        TblName = input("Provide Table name : ")
        ssquery = ("select con.[name] as constraint_name,schema_name(t.schema_id) + '.' + t.[name]  as [table],col.[name] as column_name,con.[definition],case when con.is_disabled = 0 then 'Active' else 'Disabled' end as [status] from sys.check_constraints con left outer join sys.objects t on con.parent_object_id = t.object_id left outer join sys.all_columns col on con.parent_column_id = col.column_id and con.parent_object_id = col.object_id where t.[name] like '%"+TblName+"%' order by con.name;")

# 5  
    elif msquery == 'DESCRIBE TABLE':
        print("Please notice the prompt looking for input")
        TblName2 = input("Provide Table name : ")
        ssquery = ("select schema_name(tab.schema_id) as schema_name,tab.name as table_name, col.column_id,col.name as column_name, t.name as data_type, col.max_length, col.precision from sys.tables as tab inner join sys.columns as col on tab.object_id = col.object_id left join sys.types as t on col.user_type_id = t.user_type_id where tab.name like '%"+TblName2+"%' order by schema_name,table_name, column_id;")
    elif msquery == '5':
        print("Please notice the prompt looking for input")
        TblName2 = input("Provide Table name : ")
        ssquery = ("select schema_name(tab.schema_id) as schema_name,tab.name as table_name, col.column_id,col.name as column_name, t.name as data_type, col.max_length, col.precision from sys.tables as tab inner join sys.columns as col on tab.object_id = col.object_id left join sys.types as t on col.user_type_id = t.user_type_id where tab.name like '%"+TblName2+"%' order by schema_name,table_name, column_id;")
    
# 6
    elif msquery == 'SHOW INDEX FROM TABLE':
        print("Please notice the prompt looking for input")
        Schemaname3 = input("Provide Schema name : ")
        TblName3 = input("Provide Table name : ")
        ssquery = ("DECLARE @SCHEMA VARCHAR (30); SET @SCHEMA = '"+Schemaname3+"' ;DECLARE @DB_NAME VARCHAR (30);SET @DB_NAME = '"+TblName3+"';DECLARE @OBJECTID VARCHAR (50);SET @OBJECTID = @SCHEMA+'.'+@DB_NAME;WITH myquery (Table_Name,Is_Unique, Index_Name, Column_Name,index_column_id, key_ordinal, is_included_column) AS(select 'Table_Name','Is_Unique','Index_Name','Column_Name','index_column_id','key_ordinal','is_included_column' from sys.indexes union SELECT OBJECT_NAME(a.object_id) as Table_Name, CONVERT(varchar(1), a.is_unique) AS Is_Unique,  a.name AS Index_Name, COL_NAME(b.object_id,b.column_id) AS Column_Name, CONVERT(varchar(1),b.index_column_id) AS index_column_id, CONVERT(varchar(1),b.key_ordinal) AS key_ordinal, CONVERT(varchar(1),b.is_included_column) AS is_included_column FROM sys.indexes AS a INNER JOIN  sys.index_columns AS b        ON a.object_id = b.object_id AND a.index_id = b.index_id WHERE a.is_hypothetical = 0 AND  a.object_id = OBJECT_ID(@OBJECTID) ) select * from myquery ORDER BY 2 DESC ")

    elif msquery == '6':
        print("Please notice the prompt looking for input")
        Schemaname3 = input("Provide Schema name : ")
        TblName3 = input("Provide Table name : ")
        ssquery = ("DECLARE @SCHEMA VARCHAR (30); SET @SCHEMA = '"+Schemaname3+"' ;DECLARE @DB_NAME VARCHAR (30);SET @DB_NAME = '"+TblName3+"';DECLARE @OBJECTID VARCHAR (50);SET @OBJECTID = @SCHEMA+'.'+@DB_NAME;WITH myquery (Table_Name,Is_Unique, Index_Name, Column_Name,index_column_id, key_ordinal, is_included_column) AS(select 'Table_Name','Is_Unique','Index_Name','Column_Name','index_column_id','key_ordinal','is_included_column' from sys.indexes union SELECT OBJECT_NAME(a.object_id) as Table_Name, CONVERT(varchar(1), a.is_unique) AS Is_Unique,  a.name AS Index_Name, COL_NAME(b.object_id,b.column_id) AS Column_Name, CONVERT(varchar(1),b.index_column_id) AS index_column_id, CONVERT(varchar(1),b.key_ordinal) AS key_ordinal, CONVERT(varchar(1),b.is_included_column) AS is_included_column FROM sys.indexes AS a INNER JOIN  sys.index_columns AS b        ON a.object_id = b.object_id AND a.index_id = b.index_id WHERE a.is_hypothetical = 0 AND  a.object_id = OBJECT_ID(@OBJECTID) ) select * from myquery ORDER BY 2 DESC ")

# 7
    elif msquery == 'DATABASE STATUS':
        print("Please notice the prompt looking for input")
        dbname4 = input("Provide Database Name : ")
        ssquery = ("SELECT status as status_id,                CASE                 WHEN status = 1 THEN 'New'                WHEN status = 2 THEN '2 not sure'                 WHEN status = 4 THEN 'select into/bulkcopy'                 WHEN status = 8 THEN 'trunc. log on chkpt'                 WHEN status = 16 THEN 'torn page detection'                WHEN status = 32 THEN 'loading'                 WHEN status = 64 THEN 'pre recovery'                WHEN status = 128 THEN 'recovering'                 WHEN status = 256 THEN 'not recovered'                WHEN status = 512 THEN 'offline'                 WHEN status = 1024 THEN 'read only'                 WHEN status = 2048 THEN 'dbo use only'               WHEN status = 4096 THEN 'single user'                 WHEN status = 8192 THEN '8192 not sure'                 WHEN status = 16384 THEN '16384 not sure'                 WHEN status = 32768 THEN 'emergency mode'                 WHEN status = 65536 THEN 'online'                 WHEN status = 131072 THEN '131072 not sure'                 WHEN status = 262144 THEN '262144 not sure'                 WHEN status = 524288 THEN '524288 not sure'                 WHEN status = 1048576 THEN '1048576 not sure'                 WHEN status = 2097152 THEN '2097152 not sure'                 WHEN status = 4194304 THEN 'autoshrink'                 WHEN status = 1073741824 THEN 'cleanly shutdown'                 ELSE 'None Provided' END AS 'Status_Values'            FROM sys.sysdatabases WHERE name = '"+dbname4+"'") 
    elif msquery == '7':
        print("Please notice the prompt looking for input")
        dbname4 = input("Provide Database Name : ")
        ssquery = ("SELECT status as status_id,                CASE                 WHEN status = 1 THEN 'New'                WHEN status = 2 THEN '2 not sure'                 WHEN status = 4 THEN 'select into/bulkcopy'                 WHEN status = 8 THEN 'trunc. log on chkpt'                 WHEN status = 16 THEN 'torn page detection'                WHEN status = 32 THEN 'loading'                 WHEN status = 64 THEN 'pre recovery'                WHEN status = 128 THEN 'recovering'                 WHEN status = 256 THEN 'not recovered'                WHEN status = 512 THEN 'offline'                 WHEN status = 1024 THEN 'read only'                 WHEN status = 2048 THEN 'dbo use only'               WHEN status = 4096 THEN 'single user'                 WHEN status = 8192 THEN '8192 not sure'                 WHEN status = 16384 THEN '16384 not sure'                 WHEN status = 32768 THEN 'emergency mode'                 WHEN status = 65536 THEN 'online'                 WHEN status = 131072 THEN '131072 not sure'                 WHEN status = 262144 THEN '262144 not sure'                 WHEN status = 524288 THEN '524288 not sure'                 WHEN status = 1048576 THEN '1048576 not sure'                 WHEN status = 2097152 THEN '2097152 not sure'                 WHEN status = 4194304 THEN 'autoshrink'                 WHEN status = 1073741824 THEN 'cleanly shutdown'                 ELSE 'None Provided' END AS 'Status_Values'            FROM sys.sysdatabases WHERE name = '"+dbname4+"'") 

# 8
    elif msquery == 'SHOW VIEWS':
        print("Please notice the prompt looking for input")
        SchemaName1 = input("Provide Schema name : ")
        ssquery = ("select * from information_schema.tables where table_type='view' and TABLE_SCHEMA = '"+SchemaName1+"';")
    elif msquery == '8':
        print("Please notice the prompt looking for input")
        SchemaName1 = input("Provide Schema name : ")
        ssquery = ("select * from information_schema.tables where table_type='view' and TABLE_SCHEMA = '"+SchemaName1+"';")
# 9
    elif msquery == 'INDEX FRAGMENTATION':
        print("Please notice the prompt looking for input")
        SchemaName1 = input("Provide Schema name : ")
        PCTG = input("Percentage threshold - greator then this : ")
        ssquery = ("DECLARE @SCHEMA VARCHAR (30); SET @SCHEMA = '"+SchemaName1+"' ; DECLARE @PRCNTG INT; SET @PRCNTG = '"+PCTG+"' ;  WITH myquery09 (Schma,Tble,Indx,avg_fragmentation_in_percent,page_count) AS (select 'Schema','Table','Index','avg_fragmentation_in_percent','page_count' from sys.indexes union SELECT S.name as 'Schema', T.name as 'Table', I.name as 'Index', CONVERT(varchar(20),DDIPS.avg_fragmentation_in_percent) AS 'avg_fragmentation_in_percent', CONVERT(varchar(10),DDIPS.page_count) AS 'page_count' FROM sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL, NULL, NULL) AS DDIPS INNER JOIN sys.tables T on T.object_id = DDIPS.object_id INNER JOIN sys.schemas S on T.schema_id = S.schema_id INNER JOIN sys.indexes I ON I.object_id = DDIPS.object_id AND DDIPS.index_id = I.index_id WHERE DDIPS.database_id = DB_ID() and I.name is not null and S.name = @SCHEMA AND DDIPS.avg_fragmentation_in_percent > 5) select * from myquery09 ORDER BY 4 DESC")

    elif msquery == '9':
        print("Please notice the prompt looking for input")
        SchemaName1 = input("Provide Schema name : ")
        PCTG = input("Percentage threshold - greator then this : ")
        ssquery = ("DECLARE @SCHEMA VARCHAR (30); SET @SCHEMA = '"+SchemaName1+"' ; DECLARE @PRCNTG INT; SET @PRCNTG = '"+PCTG+"' ;  WITH myquery09 (Schma,Tble,Indx,avg_fragmentation_in_percent,page_count) AS (select 'Schema','Table','Index','avg_fragmentation_in_percent','page_count' from sys.indexes union SELECT S.name as 'Schema', T.name as 'Table', I.name as 'Index', CONVERT(varchar(20),DDIPS.avg_fragmentation_in_percent) AS 'avg_fragmentation_in_percent', CONVERT(varchar(10),DDIPS.page_count) AS 'page_count' FROM sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL, NULL, NULL) AS DDIPS INNER JOIN sys.tables T on T.object_id = DDIPS.object_id INNER JOIN sys.schemas S on T.schema_id = S.schema_id INNER JOIN sys.indexes I ON I.object_id = DDIPS.object_id AND DDIPS.index_id = I.index_id WHERE DDIPS.database_id = DB_ID() and I.name is not null and S.name = @SCHEMA AND DDIPS.avg_fragmentation_in_percent > 5) select * from myquery09 ORDER BY 4 DESC")

# 10

# 11

# 12

# 13

# 14

# 15

# 16

# a
    elif msquery == 'list':
        ssquery = ("""
        You can also input corresponding number for mentioned query Ex. [cnxn.execute(scup.sqlserver('8')).fetchall()] to show views

        1. SHOW DATABASES                       2. SHOW TABLES
        3. SHOW TABLES FROM database_name       4. SHOW CHECK_CONSTRAINTS FROM TABLE
        5. DESCRIBE TABLE                       6. SHOW INDEX FROM TABLE
        7. DATABASE STATUS                      8. SHOW VIEWS
        9. INDEX FRAGMENTATION
        """)
        # print(list1)
# b   
    else:
        ssquery = ("SELECT distinct('NO MATCH FOR INPUT QUERY - RUN LIST FOR HELP') FROM sys.databases")


    return ssquery
   
    


# x = input('command input  ')
# print('you entered - ',x)
# h = sqlserver(x)
# print(h)
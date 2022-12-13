
# SHOW TABLES;  will give list alone
# SHOW FULL TABLES; will provide table type also like base table or view
# SHOW TABLES FROM database_name;

    # def show_databases():
    # return 'SELECT name FROM sys.databases;'

    #mysql to ms sql server function
def ms2mssf(msquery):

    if msquery == 'show databases':
        ssquery ='SELECT name FROM sys.databases;'
        # return ssquery
    elif msquery == 'SHOW TABLES':
        SchemaName = input("Provide Schema name : ")
        ssquery = ("SELECT table_schema, table_name, table_type FROM information_schema.tables where table_schema = '"+SchemaName+"';")
    
    elif msquery == 'SHOW TABLES FROM database_name':
        dbname = input("Provide Database name : ")
        ssquery = ("SELECT Table_Catalog, table_schema, table_name, table_type FROM information_schema.tables where Table_Catalog = '"+dbname+"';")
        return ssquery
    elif msquery == 4:
        ssquery= 'April'
    elif msquery == 5:
        ssquery= 'May'
    elif msquery == 6:
        ssquery = 'June'
    elif msquery == 7:
        ssquery = 'July'
    return ssquery
   
    


x = input('command input  ')
print('you entered - ',x)
h = ms2mssf(x)
print(h)
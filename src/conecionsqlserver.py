import pyodbc

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=172.25.0.3;DATABASE=master;UID=sa;PWD=12345')
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row  = cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)
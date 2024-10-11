import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()
SERVER = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

# '''SimpleConnection'''
# connectionString = f'''DRIVER={{SQL Server}};
#                        SERVER={SERVER};
#                        DATABASE={DATABASE};
#                        Trusted_Connection=yes'''


'''SecureConnection'''
connectionString = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                       SERVER={SERVER};
                       DATABASE={DATABASE};
                       UID={USER};
                       PWD={PASSWORD}'''

'''Display Data'''

SQL_QUERY = r'''
SELECT *
FROM products
'''

conn = pyodbc.connect(connectionString)
conn.autocommit = True
cursor = conn.cursor()
try:
    cursor.execute('USE Products')
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    for record in records:
        print(f'{record.product_id}\t{record.product_name}\t{record.price}')
except pyodbc.Error as ex:
    print(ex)
else:
    print('Data Display is Complete')
finally:
    conn.close()

# '''Insert Into Table'''
#
# SQL_QUERY = r'''
# INSERT INTO products (product_id, product_name, price)
# VALUES
# (1, "Desktop Computer", 800),
# (2, "Laptop", 1200),
# (3, "Tablet", 200),
# (4, "Monitor", 350),
# (5, "Printer", 150),
# '''
#
# conn = pyodbc.connect(connectionString)
# conn.autocommit = True
# cursor = conn.cursor()
# try:
#     cursor.execute('USE Products')
#     cursor.execute(SQL_QUERY)
# except pyodbc.Error as ex:
#     print(ex)
# else:
#     print('Data Inserted')
# finally:
#     conn.close()

# '''Ceate Table Params'''
#
# SQL_QUERY = r'''
# CREATE TABLE products
# (product_id int PRIMARY KEY,
# product_name nvarchar(50),
# price int);
# '''
#
# conn = pyodbc.connect(connectionString)
# conn.autocommit = True
# cursor = conn.cursor()
# try:
#     cursor.execute('USE Products')
#     cursor.execute(SQL_QUERY)
# except pyodbc.Error as ex:
#     print(ex)
# else:
#     print('Table Created')
# finally:
#     conn.close()

# '''Ceate DB Params'''
# SQL_COMMAND = r'''
# CREATE DATABASE Products
# ON
# (
# NAME = ProductsDatabase_data,
# FILENAME = "C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\ProductsDatabase_data.mdf",
# SIZE = 10MB,
# MAXSIZE = 20GB,
# FILEGROWTH = 5%
# )
# LOG ON
# (
# NAME = ProductsDatabase_log,
# FILENAME = "C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\ProductsDatabase_data.ldf",
# SIZE = 5MB,
# MAXSIZE = 2GB,
# FILEGROWTH = 5%
# )
# '''
#
# conn = pyodbc.connect(connectionString)
# conn.autocommit = True
# cursor = conn.cursor()
# try:
#     cursor.execute(SQL_COMMAND)
# except pyodbc.Error as ex:
#     print(ex)
# else:
#     print('Database Created')
# finally:
#     conn.close()

# SQL_QUERY = r'''
# SELECT *
# FROM Students
# '''

# conn = pyodbc.connect(connectionString)
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)
# records = cursor.fetchall()
# for record in records:
#     print(f'{record.Name}\t{record.Surname}')

# SQL_QUERY = r'''
# CREATE TABLE dbo.TestTable
# (id int PRIMARY KEY,
# TestColumn1 nvarchar(50),
# TestColumn2 nvarchar(100));
# '''
#
# conn = pyodbc.connect(connectionString)
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)



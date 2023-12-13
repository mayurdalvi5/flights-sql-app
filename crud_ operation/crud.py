import mysql.connector

# connect to database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Pass@123',
        auth_plugin='mysql_native_password',  # Specify the authentication plugin
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("Connection Established")
except Exception as e:
    print("Error:", e)

# --------------------------------
# create database on db server
# use only at the begning to create database

# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()
# ------------------------------

# create table inside indigo
#
# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()
#
# ---------------------------------------

# Insert data to the table

# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','NEW DELHI', 'IGIA'),
# (2,'CCU','KOLKATA', 'NSCA'),
# (3,'BOM','MUMBAI', 'CSMA')
# """)
# conn.commit()

# --------------------------------------------

# Search / Retrieve

mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()

print(data)
# ----------------------------------------------
# update

# mycursor.execute("""
# UPDATE airport
# SET city = 'BOMBAY'
# where airport_id = 3
# """)
# conn.commit()
# ----------------------------------------------
# Search / Retrieve
#
# mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
# data = mycursor.fetchall()
#
# print(data)
# ----------------------------------------------

#DELETE

mycursor.execute('DELETE FROM airport WHERE airport_id = 1')
conn.commit()


# select all

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

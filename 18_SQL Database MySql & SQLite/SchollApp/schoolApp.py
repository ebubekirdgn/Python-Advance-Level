import mysql.connector
from datetime import datetime
from connection import connection

mycursor = connect.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
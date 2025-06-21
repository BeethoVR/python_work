# Mysql:        python3 -m pip install mysql-connector-python --break-system-packages
# PostgreSQL:   python3 -m pip install psycopg2-binary --break-system-packages
import mysql.connector as MySqlDB
#import psycopg2        as postgresql
#import sqlite3         as sqlite
from os import system
system("clear")
print("\n\n\n")

mydb = MySqlDB.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="faureo"
                        )
mycursor = mydb.cursor()
mycursor.execute("""SELECT UsuarioId, Nombre, Login, Password
                    FROM ba_usuarios
                    WHERE (login LIKE '%NO%')""")

myresult = mycursor.fetchall()

print("\n\n\n")

for x in myresult:
  print(x)

mycursor.close()
mydb.close()
MySqlDB.MySQLConnection.close
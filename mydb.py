#Installed mysql on device
#pip install mysql
#pip install mysql-connector || mysql-connector-python
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE pluspoint")
print("All Done!!")
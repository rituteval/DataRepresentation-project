import pymysql
import mysql.connector

# Code to connect to mysql.
db = mysql.connector.connect( 
    host="localhost", 
    user ="root", 
    password ="root",
    database="ritatripadvisor"
)

cursor = db.cursor() 
sql="CREATE TABLE travelagency(ID INT AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(100), firmname VARCHAR(200), email VARCHAR(250))"
cursor.execute("drop DATABASE IF EXISTS ritatripadvisor"); # Code to drop database if CREATE repeated.
cursor.execute("create DATABASE ritatripadvisor"); # Code to create database.
cursor.execute("use ritatripadvisor"); # Use my database.
cursor.execute(sql)
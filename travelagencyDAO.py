import mysql.connector # pip install mysql.connector
from mysql.connector import cursor
import mydbconfig as cfg

class TravelagencyDAO: # Created travelagency DAO class
    db=""
   def __init__(self): # Code to connect needed database over config file
    self.db = mysql.connector.connect(
    host= cfg.mysql['localhost'],
    user=cfg.mysql['root'],
    password=   cfg.mysql['root'],
    database=   cfg.mysql['ritatripadvisor'],
    auth_plugin='mysql_native_root'
    ) 
class TravelagencyDao:
    db = ""
def __init__(self): # (constructor)
    self.db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'ritatripadvisor'
    )
            #Tested:print("so far so good, connection is made")
def create(self, travelagency):
    cursor = self.db.cursor()
    sql = "insert into travelagencies (ID, fullname, firmname, email) values (%s,%s,%s,%s)" #sql statement
    values = [
        travelagency['ID'],
        travelagency['fullname'],
        travelagency['firmname'],
        travelagency['email']    
    ]

    cursor.execute(sql, values)
    self.db.commit()
    return cursor.lastrowid
    
def getAll(self):        
    cursor = self.db.cursor()
    sql = 'select * from travelagencies'
    cursor.execute(sql)
    results = cursor.fetchall()
    returnArray = []  # converting manually
    #print(results)
    for result in results: # to take results each at a time
        resultAsDict = self.convertToDict(result)
        returnArray.append(resultAsDict)

    return returnArray

def findById(self, ID):
    cursor = self.db.cursor()
    sql = 'select * from travelagencies where ID = %s'
    values = [ ID ]
    cursor.execute(sql, values)
    result = cursor.fetchone()
    return self.convertToDict(result) 

def update(self, travelagency):
    cursor = self.db.cursor()
    sql = "update travelagencies set fullname = %s, firmname = %s, email = %s where ID = %s" #sql statement
    values = [
        travelagency['fullname'],
        travelagency['firmname'],
        travelagency['email'],
        travelagency['ID']
    
    ]
    cursor.execute(sql, values)
    self.db.commit()
    return travelagency

def delete(self, ID):
    cursor = self.db.cursor()
    sql = 'delete from travelagencies where ID = %s'
    values = [ID]
    cursor.execute(sql, values)
    
    return {}

def convertToDict(self, result): # made function
    colnames = ['ID', 'fullname', 'firmname', 'email']
    travelagency = {}
    
    if result:
        for i, colName in enumerate(colnames):
            value = result[i]
            travelagency[colName] = value
    return travelagency
        
    
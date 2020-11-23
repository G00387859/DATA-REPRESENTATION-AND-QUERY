#import mysql.connector
#from mysql.connector import cursor
import MySQLdb as sql_db
from MySQLdb import cursors
import collections

class StoreDao:
    def insert(self, product):
        mydb = sql_db.connect(
        host="localhost",
        user="donal",
        password="Hollyroco@9552",
        database="datarepresentation"
        )
        cursor = mydb.cursor()
        sql = "insert into store (productName, productType, productPrice) values (%s,%s,%s)"
        values = [
            product['productName'],
            product['productType'],
            product['productPrice']
        ]
        cursor.execute(sql, values)
        mydb.commit()
        print("done")
        return cursor.lastrowid

    def getAll(self):
        mydb = sql_db.connect(
            host="localhost",
            user="donal",
            password="Hollyroco@9552",
            database="datarepresentation"
        )
        cursor = mydb.cursor()
        sql = 'select * from store'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print("results ",results)
        returnArray = []
        for result in results:
            colnames = ['productName','productType','productPrice']
            book = {}
            if result:
               
                for i , colName in enumerate(colnames):
                    value = result[i]
                    book[colName] = value
                #print(book)
            returnArray.append(book)
        

        return returnArray 
    
    def findById(self, productName):
        mydb = sql_db.connect(
            host="localhost",
            user="donal",
            password="Hollyroco@9552",
            database="datarepresentation"
        )
        cursor = mydb.cursor()
        sql = 'select * from store where productName = %s'
        values = [ productName ]
        cursor.execute(sql, values)
        results = cursor.fetchone()
        returnArray = []
        if results:
            dictionary = {"productName":results[0],"productType": results[1],"productPrice": results[2]}
            returnArray.append(dictionary)

        return returnArray
    def update(self, product):
        mydb = sql_db.connect(
        host="localhost",
        user="donal",
        password="Hollyroco@9552",
        database="datarepresentation")
        cursor = mydb.cursor()
        sql = "update store set productType = %s,productPrice = %s where productName = %s"
        values = product['productType'],product['productPrice'],product['productName']
        cursor.execute(sql, values)
        mydb.commit()
        return product
    
    def delete(self, productName):
       mydb = sql_db.connect(
       host="localhost",
       user="donal",
       password="Hollyroco@9552",
       database="datarepresentation") 
       cursor = mydb.cursor()
       sql = 'DELETE from store where productName = %s'
       #"DELETE FROM customers WHERE address = 'Mountain 21'"
       #"DELETE FROM customers WHERE address = 'Mountain 21'"
       values = [productName]
       cursor.execute(sql, values)
       mydb.commit()
       return ""
   # mydb =""
    #def __init__(self):
        #self.db = mysql.connector.connect(
        #    host = 'localhost',
        #    user= 'donal',
        #    password = 'Hollyroco@9552',
        #    database ='datarepresentation'
        #self.mydb = sql_db.connect(
        #    host="localhost",
        #    user="donal",
        #    password="Hollyroco@9552",
        #    database="datarepresentation"
       # )
        #self.db = sql_db.connect(
        #host="localhost",
        #user="donal",
        #password="Hollyroco@9552",
        #database="datarepresentation"
    #)
        #print ("connection made")
   
    
storeDao = StoreDao()

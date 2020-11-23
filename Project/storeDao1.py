#import mysql.connector
#from mysql.connector import cursor
import MySQLdb as sql_db
from MySQLdb import cursors
import collections

class StoreDao:
    mydb = sql_db.connect(
        host="localhost",
        user="root",
        password="Hollyroco@9552",
        database="datarepresentation"
        )
    def insert(self, product):
        try:
            cursor = self.mydb.cursor()
            sql = "insert into store (productName, productType, productPrice) values (%s,%s,%s)"
            values = [
                product['productName'],
                product['productType'],
                product['productPrice']
            ]
            ret = cursor.execute(sql, values)
            print(ret)
            self.mydb.commit()
            print("done")
            return cursor.lastrowid
        except:
            return "possible database duplicate"
        

    def getAll(self):
        cursor = self.mydb.cursor()
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
        try:
            cursor = self.mydb.cursor()
            sql = 'select * from store where productName = %s'
            values = [ productName ]
            cursor.execute(sql, values)
            results = cursor.fetchone()
            returnArray = []
            if results:
                dictionary = {"productName":results[0],"productType": results[1],"productPrice": results[2]}
                returnArray.append(dictionary)

            return returnArray
        except:
            return "findById err"
        
    def update(self, product):
        try:
            cursor = self.mydb.cursor()
            sql = "update store set productType = %s,productPrice = %s where productName = %s"
            values = product['productType'],product['productPrice'],product['productName']
            cursor.execute(sql, values)
            self.mydb.commit()
            return product
        except:
            return "update error"
        
    
    def delete(self, productName):
        try:
            cursor = self.mydb.cursor()
            sql = 'DELETE from store where productName = %s'
            values = [productName]
            cursor.execute(sql, values)
            self.mydb.commit()
            return ""
        except:
            return "delete error"

storeDao1 = StoreDao()

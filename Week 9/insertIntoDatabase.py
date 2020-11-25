import MySQLdb as sql_db 
mydb = sql_db.connect(
 host="localhost",
 user="donal",
 password="Hollyroco@9552",
 database="datarepresentation"
)
cursor = mydb.cursor()
#print(cursor)
sql="select * from store"
#sql = "insert into store (productType,productName,productPrice) values (%s,%s,%s)"
#values = ("yes","beer", 13.00)
#cursor.execute(sql, values)
ret = cursor.execute(sql)
print(ret)
#mydb.commit()
print("1 record inserted, ID:", cursor.lastrowid)
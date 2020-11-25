import MySQLdb as sql_db 
mydb = sql_db.connect(
 host="localhost",
 user="donal",
 password="Hollyroco@9552",
 database="datarepresentation"
)
cursor = mydb.cursor()
sql="CREATE TABLE student (id int NOT NULL auto_increment,firstname varchar(100),age int(3),PRIMARY KEY(id))"
cursor.execute(sql)
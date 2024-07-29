import mysql.connector
mydb=mysql.connector.connect
host="DESKTOP-VUCA74I"
user="nagendra"
password="cbkph"
database="new"
mycusor=mydb.cusor()
query="select * for tablename"
mycusor.execute(query)
result=mycusor.fetchall()
for row in result:
    print(row)
mycusor.close()
mydb.close()
    
    

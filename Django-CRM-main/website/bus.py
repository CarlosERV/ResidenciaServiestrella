import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '',
    db='elderco'
	)

cursor = dataBase.cursor()
cursor.execute("SELECT * FROM website_record WHERE first_name LIKE '%i%' or last_name LIKE '%i%';")
r=cursor.fetchall()
print(r)
import sqlite3

db = sqlite3.connect('sugarDataMonitor.db')
c = db.cursor()
# query = 'CREATE TABLE sugarinsulin (id INTEGER PRIMARY KEY AUTOINCREMENT , dose int, iType VARCHAR(50), interval VARCHAR(50), date VARCHAR(50), sValue INTEGER )'
q = 'SELECT * FROM sugarinsulin ORDER BY date ASC'
c.execute(q)
data = c.fetchall()
print(data)
c.close()
db.commit()
db.close()

# d = {'name':"Mohit"}
# print(list(d.keys())[0])
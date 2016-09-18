import MySQLdb

db = MySQLdb.connect(host="localhost",  
                     user="",         
                     passwd="",
                     db="")    


cur = db.cursor()


cur.execute("SELECT * FROM PRICINGAPP.TICKER")


for row in cur.fetchall():
    print row[0]

db.close()

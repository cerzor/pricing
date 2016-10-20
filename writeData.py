import MySQLdb
def writeData(statements):
    db = MySQLdb.connect(host="localhost",  
                         user="price",         
                         passwd="testApp123",
                         db="PRICINGAPP")    


    cur = db.cursor()

    try:
        for statement in statements:
            cur.execute(statement)
            cur.execute("commit")
    except:
        print "Unexpected error at WRITING DATA"
        raise


#    results = []
#    try:
#        for row in cur.fetchall():
#            results.append(row[0])
#    except:
#        print "Unexpected error at WRITING DATA"

    try:
        cur.close()
        db.close()
#        print results
    except:
        print "FAILURE TO CLOSE DB WRITING DATA"

    return "SUCCESS"
#pullSymbols()

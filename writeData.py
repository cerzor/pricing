import MySQLdb
def writeData(statements, pw):
    db = MySQLdb.connect(host="localhost",  
                         user="price",         
                         passwd=pw,
                         db="PRICINGAPP")    


    cur = db.cursor()

    try:
        for statement in statements:
            cur.execute(statement)
            cur.execute("commit")
    except:
        print "Unexpected error at WRITING DATA"
        print "statement"
        return "FAIL"


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

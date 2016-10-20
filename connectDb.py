import MySQLdb
def pullSymbols():
    db = MySQLdb.connect(host="localhost",  
                         user="",         
                         passwd="",
                         db="")    


    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM PRICINGAPP.TICKER where SYMBOL='AMD' or SYMBOL='MRO' or SYMBOL='NRG' or SYMBOL = 'FB' or SYMBOL = 'MITT^B'")
    except:
        print "Unexpected error at PULL SYMBOLS"
        raise


    results = []
    try:
        for row in cur.fetchall():
            results.append(row[0])
    except:
        print "Unexpected error at PRINT RS"

    try:
        cur.close()
        db.close()
#        print results
    except:
        print "FAILURE TO CLOSE DB"

    return results
#pullSymbols()

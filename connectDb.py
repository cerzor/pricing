import MySQLdb
def pullSymbols(pw):
    db = MySQLdb.connect(host="localhost",  user="price",passwd=pw, db="PRICINGAPP")


    cur = db.cursor()

    try:
        cur.execute("SELECT distinct  case when LEFT(SYMBOL, INSTR(SYMBOL,'^') - 1 ) != '' then LEFT(SYMBOL, INSTR(SYMBOL,'^') - 1 )  else symbol end SYMBOL FROM PRICINGAPP.TICKER")
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

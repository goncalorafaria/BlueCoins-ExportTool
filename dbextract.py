from sqlite3 import *
import csv
import sys

if len(sys.argv) > 1:
    dbname = sys.argv[1]
else:
    dbname = "*.fydb"

if len(sys.argv) > 2:
    csvname = sys.argv[2]
else:
    csvname = "output.csv"

with connect(dbname) as conn :

    cur = conn.cursor()

    rset = cur.execute( 
        'SELECT ' 
		    ' (CAST(T.amount  AS float) / 1000000.0) as Cost, '
		    'I.itemName as "Expense Name",'
		    'T.date as Date,' 
		    'A.accountName as Payment,'
		    'C.childCategoryName as Category '
	    'FROM TRANSACTIONSTABLE as T, '
		    'ITEMTABLE as I, '
		    'ACCOUNTSTABLE as A, '
		    'CHILDCATEGORYTABLE as C '
		'WHERE T.itemID == I.itemTableID and ' 
		    'T.amount != 0 and '
		   ' A.accountsTableID == T.accountID and ' 
            ' C.categoryTableID == T.categoryID' )

    rows = cur.fetchall()

    with open(csvname, "w") as csvfile:
        csvWriter = csv.writer(csvfile)

        csvWriter.writerows(rows)



import mysql.connector
from mysql.connector import Error

def retrieveAccountData():
    listStore = []
    listReturn = []
    try:
       mySQLconnection = mysql.connector.connect(host='localhost',
                                 database='dbschema',
                                 user='Admin',
                                 password='cz3003ransack')
       
       sql_select_Query = "select * from account"
       cursor = mySQLconnection .cursor()
       cursor.execute(sql_select_Query)
       records = cursor.fetchall()
    
       for row in records:
           listStore = []
           """
           print("ID = ", row[0], )
           print("username = ", row[1])
           print("password  = ", row[2])
           """
           listStore.append(row[1])
           listStore.append(row[2])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection .is_connected()):
            mySQLconnection.close()
            print("\nMySQL connection is closed Now")
    
    print("Success")
    return listReturn
    
  
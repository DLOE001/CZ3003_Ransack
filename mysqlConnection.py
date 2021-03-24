import mysql.connector
from mysql.connector import Error

# Extract the mySQLconnection for easier re-usability
def __mySQLconnection():
    mySQLconnection = mysql.connector.connect(host='localhost',
                                 database='dbschema',
                                 user='Admin',
                                 password='cz3003ransack')
    
    return mySQLconnection

### General Functions ###

# Retrieves all Student account data
def retrieveStudentAccountData():
    listStore = []
    listReturn = []
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from student"
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listStore = []
           listStore.append(row[1])
           listStore.append(row[2])
           listStore.append(row[3])
           listStore.append(row[4])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            #print("\nMySQL connection is closed Now")
    
    return listReturn

# Retrieves all Teacher account data
def retrieveTeacherAccountData():
    listStore = []
    listReturn = []
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from teacher"
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listStore = []
           listStore.append(row[1])
           listStore.append(row[2])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            #print("\nMySQL connection is closed Now")
    
    return listReturn

# Retrieves all Quiz Level data
def retrieveQuizLevelData(worldSelected, levelSelected):
    listStore = []
    listReturn = []
    queryLevelSelected = ((worldSelected-1)*3) + levelSelected
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select quizID, levelID, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3 from quiz \
                   WHERE levelID = %d;" % (queryLevelSelected)
       
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listStore = []
           listStore.append(row[0])
           listStore.append(row[1])
           listStore.append(row[2])
           listStore.append(row[3])
           listStore.append(row[4])
           listStore.append(row[5])
           listStore.append(row[6])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            #print("\nMySQL connection is closed Now")
            
    return listReturn



### Student Specific Functions ###

# Create a Student Account
def createStudentAccount(username, password, email):
    listStore = []
    listReturn = []
    worldsCleared = 0
    title = "Newbie"
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "INSERT INTO student (username, password, email, title, worldsCleared) \
                    VALUES ('%s', '%s', '%s', '%s', %d);" % (username, password, email, title, worldsCleared)
                    
    
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       mySQLconnection.commit()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            #print("\nMySQL connection is closed Now")
        
# Retrieve Top 5 student records based on overall score for story mode
def retrieveLeaderboard():
    listStore = []
    listReturn = []
    
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "SELECT s.title, sls.username, SUM(score) from storylevelscore sls \
                    JOIN student s ON sls.username = s.username \
                    GROUP BY sls.username \
                    ORDER BY SUM(score) DESC;"
       
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listStore = []
           listStore.append(row[0])
           listStore.append(row[1])
           listStore.append(row[2])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            
    return listReturn
            
### Quiz Score Functions ###

# Retrieve User Quiz Score
def retrieveUserQuizScore(username, level):
    listStore = []
    listReturn = []
    
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select score from storylevelscore \
                   WHERE username = '%s' AND levelID = %d;" % (username, level)
       
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listStore = []
           listStore.append(row[0])
           listReturn.append(listStore)
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            
    return listReturn

# Update User Quiz Score
def updateUserQuizScore(username, level, score):
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "UPDATE storylevelscore \
                    SET score = %d \
                    WHERE username = '%s' AND levelID = %d;" % (score, username, level)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()

# Add User Quiz Score
def insertUserQuizScore(username, level, score):
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "INSERT INTO storylevelscore \
                    VALUES('%s', %d, %d);" % (username, level, score)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()    


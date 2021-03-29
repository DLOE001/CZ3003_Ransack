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

# Retrieves all Custom Quiz Name data
def retrieveCustomQuizNames():
    listReturn = []
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select quizName from customcreatedquiz"
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()
    
       # For each record in the DB, append it to the return list
       for row in records:
           listReturn.append(row[0])
       cursor.close()
    
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            #print("\nMySQL connection is closed Now")
    
    return listReturn

# Retrieves all Custom Quiz Name data
def retrieveAllCustomQuiz():
    listStore = []
    listReturn = []
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from customcreatedquiz"
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
           listStore.append(row[7])
           listStore.append(row[8])
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

# Retrieves specific custom quiz data
def retrieveStudentCustomQuiz(quizName):
    listStore = []
    listReturn = []
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select customQuizID, quizName, question, answer, wrongAnswer1, wrongAnswer2 \
                , wrongAnswer3 from customcreatedquiz \
                  WHERE quizName = '%s'" % (quizName)
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

# Retrieves all pending Custom Quiz Name data
def retrievePendingCustomQuiz(createdBy):
    listStore = []
    listReturn = []
    status = "Pending"
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from customcreatedquiz \
                   WHERE createdBy = '%s' AND \
                   status = '%s'" % (createdBy, status)
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
           listStore.append(row[7])
           listStore.append(row[8])
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

# Retrieves all pending Custom Quiz Name data
def retrieveAllPendingCustomQuiz():
    listStore = []
    listReturn = []
    status = "Pending"
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from customcreatedquiz \
                   WHERE status = '%s'" % (status)
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
           listStore.append(row[7])
           listStore.append(row[8])
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

# Retrieves all approved Custom Quiz Name data
def retrieveApprovedCustomQuiz():
    listStore = []
    listReturn = []
    status = "Approved"
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "select * from customcreatedquiz \
                   WHERE status = '%s';" % (status)
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
           listStore.append(row[7])
           listStore.append(row[8])
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

# Add Student Custom Quiz Score
def retrieveStudentCustomQuizScore(customQuizID, quizName, username):
    listStore = []
    listReturn = []
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "SELECT score FROM customquizscore \
                    WHERE customQuizID = %d \
                    AND quizName = '%s' \
                    AND username = '%s';"  % (customQuizID, quizName, username)
       
        
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

# Add Student Custom Quiz Score
def insertStudentCustomQuizScore(customQuizID, quizName, username, score):
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "INSERT INTO customquizscore \
                    VALUES(%d,'%s', '%s', %d);" % (customQuizID, quizName, username, score)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()  
    
# Update Custom Quiz Score/Attempt
def updateStudentCustomQuizScore(customQuizID, quizName, username, score):

    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "UPDATE customquizscore \
                    SET score = %d \
                    WHERE customQuizID = %d \
                    AND quizName = '%s' \
                    AND username = '%s'" % (score, customQuizID, quizName, username)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()

# Update Custom Quiz Rating
def updateCustomQuizRating(quizName, newRating):

    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "UPDATE customcreatedquiz \
                    SET rating = %d \
                    WHERE quizName = '%s'" % (newRating, quizName)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            
# Create a Custom Quiz Account
def createCustomQuiz(createdBy, quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
    listStore = []
    listReturn = []
    rating = 0
    status = "Pending"
    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "INSERT INTO customcreatedquiz (createdBy, quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3, rating, status) \
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s');" % (createdBy, quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3, rating, status)
                    
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
 
# Retrieve Friend List
def retrieveFriendList(username):

    try:
       mySQLconnection = __mySQLconnection()
       sqlQuery = "SELECT friendlist from student \
                   WHERE username = '%s';" % (username)
       
       cursor = mySQLconnection.cursor()
       cursor.execute(sqlQuery)
       records = cursor.fetchall()

    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()

    #Covert from tuple to list
    recordslist = list(records)

    #Covert from index 0 of list (contains the names) to string
    recordsstring = str(recordslist[0])

    # Cut the string so to only contain names
    recordsstring = recordsstring[2:-3]

    # Spilt into list
    recordslist = recordsstring.split(", ")

    print(recordslist)
            
    return recordslist

# Update Friend List
def updateFriendList(username, newfriendstring):
    
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "UPDATE student \
                    SET friendlist = '%s' \
                    WHERE username = '%s';" % (newfriendstring, username)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
    
    print("Updated")
    
### Teacher Specific Functions ###

# Approves the User Created Custom Quiz
def updateUserCustomQuizStatus(quizName, decision):
    status = decision
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "UPDATE customcreatedquiz \
                    SET status = '%s' \
                    WHERE quizName = '%s';" % (status, quizName)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
    
    print("Updated")

# Approves the User Created Custom Quiz
def removeRejectedCustomQuiz():
    rejected = "Rejected"
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "DELETE FROM student \
                    WHERE status = '%s';" % (rejected)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
    
    print("Updated")
    
# Remove Selected Custom Quiz
def removeStudentCustomQuiz(quizName):
    try:
        mySQLconnection = __mySQLconnection()
        sqlQuery = "DELETE FROM customcreatedquiz \
                    WHERE quizName = '%s';" % (quizName)
       
        cursor = mySQLconnection.cursor()
        cursor.execute(sqlQuery)
        mySQLconnection.commit()
        
    except Error as e :
        print ("Error connecting MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
    
    print("Updated")
    

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


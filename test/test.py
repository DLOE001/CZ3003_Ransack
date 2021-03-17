from account import Account
import mysqlConnection

"""
allUsers = mysqlConnection.retrieveStudentAccountData()

print(allUsers)
print()

for i in allUsers:
    print("username = ", i[0])
    print("password  = ", i[1])
    print("email  = ", i[2])
    print("rank  = ", i[3])
    print()
"""

mysqlConnection.createStudentAccount("Tom", "Nice", "")


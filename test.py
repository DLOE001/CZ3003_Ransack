from account import Account
import mysqlConnection

allUsers = mysqlConnection.retrieveAccountData();

print(allUsers)
print()

for i in allUsers:
    print("username = ", i[0])
    print("password  = ", i[1])
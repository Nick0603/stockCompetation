import mysql.connector
import sys

user = 'root'
pwd  = 'root'
host = 'localhost'
db   = 'stockcompetition'

def UpdateRatio(Accounts):
    
    update_sql = "Update  teams Set Ratio = {2} Where teamID = {1}"

    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()

    try:
        for Account in Accounts:
            update_sql = "Update  teams Set Ratio = {} Where teamID = {}".format(Account.ratio,Account.teamId)
            cursor.execute(update_sql)
    except mysql.connector.Error as err:
        print("Update  table 'teamRatio' failed.")
        print("Error: {}".format(err.msg))
        sys.exit()

    cnx.commit()
    cursor.close()
    cnx.close()

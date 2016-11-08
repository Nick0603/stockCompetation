import mysql.connector
import sys

user = 'root'
pwd  = 'root'
host = '127.0.0.1'
db   = 'StockCompetation'

def UpdateRatio(teamIds,Ratios):
    try:
        for ID in teamIds:
            if not(isinstance(ID,int)):
               raise Exception('ErrorInput (id)')
        for Ratio in Ratios:
            if not(isinstance(Ratio,float)):
                raise Exception('ErrorInput (Ratio)')
        if len(teamIds) != len(Ratios) :
                raise Exception('ErrorInput (Ratio.len != Ratio.len)')
    except Exception as inst:
        print(inst)


    update_sql = "Update  teamRatios Set Ratio = {2} Where teamID = {1}"

    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()

    try:
        for index in range(0,len(teamIds)):
            update_sql = "Update  teamRatios Set Ratio = {} Where teamID = {}".format(Ratios[index],teamIds[index])
            cursor.execute(update_sql)
    except mysql.connector.Error as err:
        print("Update  table 'teamRatio' failed.")
        print("Error: {}".format(err.msg))
        sys.exit()

    cnx.commit()
    cursor.close()
    cnx.close()

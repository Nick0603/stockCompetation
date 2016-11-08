#encoding:UTF-8
import urllib.request
import json
import datetime
import MySQLUpdate
import time

def getAccountInfo(id):
    url = "http://www.cmoney.tw/vt/ashx/accountdata.ashx?act=AccountInfo&aid=" + str(id)
    res = urllib.request.urlopen(url).read()
    res = res.decode('UTF-8')
    data = json.loads(res)
    return data

def getInventoryDetail(id):
    url = "http://www.cmoney.tw/vt/ashx/accountdata.ashx?act=InventoryDetail&aid=" + str(id)
    res = urllib.request.urlopen(url).read()
    res = res.decode('UTF-8')
    data = json.loads(res)
    return data

def getAccountRatio(id):
    data = getAccountInfo(id)
    Ratio = data['Ratio']
    return Ratio

class Account:
    def __init__(self,teamId,AccountId,ratio):
                    self.teamId = teamId
                    self.AccountId = AccountId
                    self.name = 'test'
                    self.ratio = ratio

def displayNowTime():
    nowTime = datetime.datetime.now();
    Date_text = nowTime.strftime('%y/%m/%d')
    Time_text = nowTime.strftime('%H:%M:%S')
    print("資訊更新!!：{date}  {time}".format(date=Date_text,time=Time_text))


def catchAccountDate(Accounts,AccountIds):
    for i in range(0,Amount):
        teamId = AccountIds[i]
        if type(teamId) == list:
            totalRatio = 0
            for singleId in teamId:
                totalRatio += float(getAccountRatio(singleId))
            Ratio = totalRatio/len(teamId)
        elif teamId != i+1 :
            Ratio = float(getAccountRatio(teamId))
        else:
            Ratio = -1000
        Accounts.append(Account(i+1,teamId,Ratio))

Amount = 12;

AccountIds = [212876,211616,211022,216339,211135,212882,[212988,212848,212987],212459,211283,211024,211044,211020]

while(1):
    Accounts = []
    catchAccountDate(Accounts,AccountIds)
    MySQLUpdate.UpdateRatio(Accounts)

    print("----------------------------------------")
    displayNowTime()
    
    time.sleep(5)

#encoding:UTF-8
import urllib.request
import json
import datetime
import MySQLUpdate
import time
from bs4 import BeautifulSoup

def getTeamName(id):
    url = "http://www.cmoney.tw/vt/account-profile-info.aspx?account=" + str(id)
    res = urllib.request.urlopen(url).read()
    res = res.decode('UTF-8')
    soup = BeautifulSoup(res, "html.parser")

    headerTitle = soup.find('header', {'class': 'title'})
    if headerTitle == None:
        
        print("headerTitle NOT FOUND!!")
        return 0
    teamName = headerTitle.contents[1]
    return teamName


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
    def __init__(self,teamId,AccountId,Name,ratio):
                    self.teamId = teamId
                    self.AccountId = AccountId
                    self.Name = Name
                    self.ratio = ratio

def displayNowTime():
    nowTime = datetime.datetime.now();
    Date_text = nowTime.strftime('%y/%m/%d')
    Time_text = nowTime.strftime('%H:%M:%S')
    print("資訊更新!!：{date}  {time}".format(date=Date_text,time=Time_text))


def catchAccountDate(Accounts,AccountIds):
    for i in range(0,len(AccountIds)):
        teamId = AccountIds[i]
        if type(teamId) == list: #當組別帳戶有超過1個時候(例外情形  戶名只取第一個)
            totalRatio = 0
            for singleId in teamId:
                totalRatio += float(getAccountRatio(singleId))
            Ratio = totalRatio/len(teamId)
                
        elif teamId != i+1 : #如果ID不是未填寫  (未填寫狀態是直接填上組別編號)
            Ratio = float(getAccountRatio(teamId))
        else: # 未填寫ID是直接填上組別編號
            Ratio = -1000
            
        Accounts[i].ratio = Ratio


#主程式開始點
#如果ID是未填寫  (未填寫狀態是直接填上組別編號)

Accounts = []
AccountIds = [212876,211616,211022,216339,211135,212882,[212988,212848,212987],212459,211283,211024,211044,211020]

delayTime = int( input ('Please input the Update delayTime ( T > 5s ):  ') )
while(delayTime < 5):
    delayTime = int( input ('Please input the Update delayTime ( T > 5s ):  '))

#初始化 (創建帳戶及收尋團隊名稱)
Accounts = []
for i in range(0,len(AccountIds)):
    teamId = AccountIds[i]
    if type(teamId) == list: #當組別帳戶有超過1個時候(例外情形  戶名只取第一個)
        TeamName = getTeamName(teamId[0])
    elif teamId != i+1 : #如果ID不是未填寫  (未填寫狀態是直接填上組別編號)
        TeamName = getTeamName(teamId)
    else: # 未填寫ID是直接填上組別編號
        TeamName = 'null'
        
    Accounts.append(Account(i+1,teamId,TeamName,0))



#更新資料
while(True):
    catchAccountDate(Accounts,AccountIds)
    MySQLUpdate.UpdateRatio(Accounts)

    print("----------------------------------------")
    displayNowTime()
    time.sleep(delayTime)




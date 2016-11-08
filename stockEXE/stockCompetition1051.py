#encoding:UTF-8
import urllib.request
import json
import datetime
import os

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

def displayRank(Sort_Account):
    
    count = 0
    rank = 0
    for Account in Sort_Account:
        rank +=1
        if Account.ratio == -1000:
            count += 1
        else:
            result = "目前第%3d名 組別：%2d 總報酬率：%5.3f%%" %(rank,Account.teamId,Account.ratio)
            print(result)

    if count >0:
        print("未讀取的到的隊伍帳號數目：%d"%count)
        
def displayAccountStatus(Accounts):
        for Account in Accounts:
            if Account.ratio == -1000:
                result = "目前組別：%2d  總報酬率：無法讀取資料" %(Account.teamId)
            else:
                result = "目前組別：%2d 總報酬率：%5.3f%%" %(Account.teamId,Account.ratio)
            print(result)

def displayNowTime():
    nowTime = datetime.datetime.now();
    Date_text = nowTime.strftime('%y/%m/%d')
    Time_text = nowTime.strftime('%H:%M:%S')
    print("今天日期：{date} 現在時間：{time}".format(date=Date_text,time=Time_text))

def catchAccountDate(Accounts,AccountIds):
    for i in range(0,Ammount):
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


Ammount = 12;
AccountIds = [212876,211616,211022,216339,211135,212882,[212988,212848,212987],212459,211283,211024,211044,211020]

while(1):
    Accounts = []
    catchAccountDate(Accounts,AccountIds)
    sort_Accounts= sorted(Accounts,key=lambda x: x.ratio,reverse = True)

    displayNowTime()
    print("----------------------------------------")
    displayRank(sort_Accounts)
    print("----------------------------------------")
    displayAccountStatus(Accounts)
    print("----------------------------------------")


    
    mode = input('按下Enter鍵重新載入資料')
    print('\n'*30)

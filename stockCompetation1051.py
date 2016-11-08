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

Ammount = 12;

ids = [212876,211616,211022,4,211135,212882,[212988,212848,212987],212459,211283,211024,211044,211020]

while(1):
    
    Ratioes = []
    for i in range(0,Ammount):
        id = ids[i]
        if type(id) == list:
            totalRatio = 0
            for singleId in id:
                totalRatio += float(getAccountRatio(singleId))
            AverageRatio = totalRatio/len(id)
            Ratioes.append(AverageRatio)
        elif id != i+1 :
            Ratioes.append(float(getAccountRatio(id)))
        else:
            Ratioes.append(-1000)

    sort_Ratioes = sorted(Ratioes,reverse = True)

    print("----------------------------------------")
    nowTime = datetime.datetime.now();
    Date_text = nowTime.strftime('%y/%m/%d')
    Time_text = nowTime.strftime('%H:%M:%S')
    print("今天日期：{date} 現在時間：{time}".format(date=Date_text,time=Time_text))
    
    count = 0
    for i in range(0,Ammount):
        Ratio = sort_Ratioes[i]
        teamNum = Ratioes.index( Ratio)
        #index = floatIndex(Ratioes,sort_Ratioes[i])
        #index 收尋到第一個不會顯示 list第0  會顯示-1

        if Ratio == -1000:
            count += 1
        else:
            result = "目前第%3d名 組別：%2d 總報酬率：%5.3f%%" %(i+1,teamNum+1,Ratio)
            print(result)
        
    for index in range(0,count):
        result = "目前第%3d名 組別：未知  總報酬率：未知"%(i+1)
        print(result)
    print("----------------------------------------")
    
    index = 0
    for i in Ratioes:
        if Ratioes[index] == -1000:
            result = "目前組別：%2d  總報酬率：無法讀取資料" %(index+1)
        else:
            result = "目前組別：%2d 總報酬率：%5.3f%%" %(index+1,Ratioes[index])
        index +=1
        print(result)

    print("----------------------------------------")
    mode = input('按下Enter鍵重新載入資料')
    print('\n'*30)

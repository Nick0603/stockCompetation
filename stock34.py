#encoding:UTF-8
import urllib.request
import json
import datetime

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

def floatIndex(my_list,f):
    for i in range(1,len(my_list)):
        listdata = my_list[i]
        if(listdata == f):
            return i
    return -1

Ammount = 12;

ids = [212876,211616,211022,4,211135,212882,7,212459,211283,211024,211044,211020]

while(1):
    
    Ratioes = []
    for i in range(0,Ammount):
        id = ids[i]
        if(id != i+1):
            Ratioes.append(float(getAccountRatio(id)))
        else:
            Ratioes.append(-1000)

    sort_Ratioes = Ratioes[:]
    sort_Ratioes.sort(reverse = True)

    print("----------------------------------------")
    nowTime = datetime.datetime.now();
    Date_text = nowTime.strftime('%y/%m/%d')
    Time_text = nowTime.strftime('%H:%M:%S')
    print("今天日期：{date} 現在時間：{time}".format(date=Date_text,time=Time_text))
    
    for i in range(0,Ammount):
        Ratio = sort_Ratioes[i]
        index = floatIndex(Ratioes,sort_Ratioes[i])
        
        if Ratio != -1000:      
            result = "目前第%2d名 組別：%2d 總報酬率：%5.3f%%" %(i+1,index+1,Ratio)
            print(result)

    print("----------------------------------------")
    for i in range(0,Ammount):
        if Ratioes[i] == -1000:
            result = "目前組別：%2d 無法讀取到帳戶資料"%(i+1)
            print(result)

    print("----------------------------------------")
    mode = input('按下Enter鍵重新載入資料')

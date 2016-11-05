#encoding:UTF-8
import urllib.request
import json

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

ids = [0,212876,2,211022,4,211135,212882,7,212459,211283,211024,211044,211020]
Ratioes = [0]
for i in range(1,Ammount):
    id = ids[i]
    if(id != i):
        Ratioes.append(float(getAccountRatio(id)))
    else:
        Ratioes.append(-1000)


sort_Ratioes = Ratioes[:]
sort_Ratioes.sort(reverse = True)

for i in range(1,Ammount):
    Ratio = sort_Ratioes[i]
    index = floatIndex(Ratioes,sort_Ratioes[i])
    
    if Ratio != -1000:      
        result = "目前第%2d名 組別：%2d 總報酬率：%5.3f%%" %(i,index,Ratio)
        print(result)
    
for i in range(1,Ammount):
    if Ratioes[i] == -1000:
        result = "目前組別：%2d 無法讀取到帳戶資料"%i 
        print(result)


import json
"""
json格式基本觀念

物件：一般用大括號{ }表示
陣列：一般用中括號[ ]表示

Python應用在json字串的形式資料

使用dumps()將python資料轉換成json格式

dumps()的sort_keys參數：使用sort_keys=True可以將轉成json格式的物件排序
dumps()的indent參數：設定縮排json物件的鍵值，讓json物件可以更容易顯現
顯示所儲存的中文資料：

1.encoding='utf-8'
2.ensure_ascii=False

with open(fn,encoding='utf-8') as fnObj:
    json.dump(objlist,fnObj,ensure_ascii=False)
        

"""

"""
listNumbers=[5,10,20,1] #串列資料
tupleNumbers=(1,5,10,9) #元組資料
jsonData1=json.dumps(listNumbers)  # 將串列資料轉換成json資料
jsonData2=json.dumps(tupleNumbers) # 將串列資料轉換成json資料

print(jsonData1)
print(jsonData2)
print("json陣列在python的資料型態",type(jsonData1))  #在python的儲存方式為'[5,10,20,1]'

"""

"""

# 將一個字典資料儲存成json檔案

dictObj={'b':80, 'a':25, 'c':60}
fn = 'out1_8.json'
with open(fn,'w') as fnObj:
    json.dump(dictObj,fnObj)

# dump()方法的第一個參數是欲儲存成json格式的資料，第二個是欲儲存成的檔案物件

"""

"""
# 簡單的json檔案應用

fn = 'out1_82.json'
login=input("請輸入帳號 ：")
with open(fn,'w') as fnObj:
     json.dump(login,fnObj)
     print("%s!歡迎使用本系統" %login)

# %s:取得輸入到json檔案中的資料

"""
"""

fn ='login_13.json'
try:
    with open(fn) as fnObj:
        login1=json.load(fnObj)
except Exception:
    login1=input("請輸入帳號：")
    with open(fn,'w') as fnObj:
        json.dump(login1,fnObj)
        print("系統已記錄你的帳號")
else:
    print("%s 歡迎回來" %login1)

#   print("%s(輸入的值)" %輸入值所存取的變數)      

#try:
    # 嘗試一些程式碼
#except:
    # 當程式出現異常時執行這邊的程式碼

"""

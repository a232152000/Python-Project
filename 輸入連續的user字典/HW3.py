#-*- coding: big5 -*-
import collections
import json

def TestInput(nameID):
    for i in ans:
        if(i.count(nameID)!=False):
            print("\n編號輸入重複，請重新輸入")
            return False
            
def GetName():
    data=raw_input("\n輸入空格作為下筆資料，以輸入enter表結束:")
    data=data.split(" ")

    for i in data:
        data1=i.split(":")
        firstName = data1[0]
        lastName  = data1[1]
        nameID    = data1[2]
        part      = data1[3]
        #測試編號輸入
        if(TestInput(nameID)==False):
            break
        
        result=NameProcess(firstName+lastName)
        #print(result)
        usernames.append(result)
        ans.append(User(result,firstName,lastName,nameID,part))

        ListToDict(nameID)

def NameProcess(data):
    count=usernames.count(data)+1
    while True:
        if(usernames.count(data + "_" + str(count)) == 1):
            count+=1
        else:
            break
            
    if(count!=1):
        return data + "_" + str(count-1)
    else:
        return data
    
def ListToDict(nameID):
    users[nameID] = ans[len(ans)-1]

    
def NameShow():
    for i in ans:
        print("姓名:{0} 姓:{1} 名:{2} 編號:{3} 部門:{4} "
                  .format(i.Name, i.FirstName, i.LastName, i.NameID, i.Part))

  
User=collections.namedtuple("User","Name FirstName LastName NameID Part")
usernames = []
ans = []
users = dict()
print("\n範例:張:皓博:02360706:資工系")

while(True):
    print("\n")
    GetName()
    print("\n~~~~~~~~~~~~print(users)~~~~~~~~~~~~")
    print str(users).decode('string_escape')
    print("\n~~~~~~~~~~~~json~~~~~~~~~~~~")
    print(json.dumps(users,encoding="utf-8", ensure_ascii=False))
    print("\n~~~~~~~~~~~~所有資料~~~~~~~~~~~~")
    NameShow()
    
    loop = raw_input("\n繼續輸入請按'Y'，不想輸入請按'N':")
    if(loop=="N"):
        break

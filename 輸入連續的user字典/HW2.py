#張:皓博:02360706:資工系 張:皓博:02360706:資工系

import collections

def GetName():
    data=raw_input("(輸入空格作為下筆資料)(以輸入enter表結束):")
    data=data.split(" ")

    for i in data:
        data1=i.split(":")
        firstName = data1[0]
        lastName  = data1[1]
        nameID    = data1[2]
        part      = data1[3]

        result=NameProcess(firstName+lastName)
        print(result)
        usernames.append(result)
        ans.append(User(result,firstName,lastName,nameID,part))
        
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

def NameShow():
    for i in ans:
        print("姓名:{0} 姓:{1} 名:{2} 編號:{3} 部門:{4} "
                  .format(i.Name, i.FirstName, i.LastName, i.NameID, i.Part))
    
User=collections.namedtuple("User","Name FirstName LastName NameID Part")
usernames = []
ans = []
print("範例:張:皓博:02360706:資工系 張:皓博:02360706:資工系")
GetName()
print("~~~~~~~~~~~~所有資料~~~~~~~~~~~~")
NameShow()

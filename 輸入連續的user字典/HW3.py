#-*- coding: big5 -*-
import collections
import json

def TestInput(nameID):
    for i in ans:
        if(i.count(nameID)!=False):
            print("\n�s����J���ơA�Э��s��J")
            return False
            
def GetName():
    data=raw_input("\n��J�Ů�@���U����ơA�H��Jenter����:")
    data=data.split(" ")

    for i in data:
        data1=i.split(":")
        firstName = data1[0]
        lastName  = data1[1]
        nameID    = data1[2]
        part      = data1[3]
        #���սs����J
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
        print("�m�W:{0} �m:{1} �W:{2} �s��:{3} ����:{4} "
                  .format(i.Name, i.FirstName, i.LastName, i.NameID, i.Part))

  
User=collections.namedtuple("User","Name FirstName LastName NameID Part")
usernames = []
ans = []
users = dict()
print("\n�d��:�i:�q��:02360706:��u�t")

while(True):
    print("\n")
    GetName()
    print("\n~~~~~~~~~~~~print(users)~~~~~~~~~~~~")
    print str(users).decode('string_escape')
    print("\n~~~~~~~~~~~~json~~~~~~~~~~~~")
    print(json.dumps(users,encoding="utf-8", ensure_ascii=False))
    print("\n~~~~~~~~~~~~�Ҧ����~~~~~~~~~~~~")
    NameShow()
    
    loop = raw_input("\n�~���J�Ы�'Y'�A���Q��J�Ы�'N':")
    if(loop=="N"):
        break

#�i:�q��:02360706:��u�t �i:�q��:02360706:��u�t

import collections

def GetName():
    data=raw_input("(��J�Ů�@���U�����)(�H��Jenter����):")
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
        print("�m�W:{0} �m:{1} �W:{2} �s��:{3} ����:{4} "
                  .format(i.Name, i.FirstName, i.LastName, i.NameID, i.Part))
    
User=collections.namedtuple("User","Name FirstName LastName NameID Part")
usernames = []
ans = []
print("�d��:�i:�q��:02360706:��u�t �i:�q��:02360706:��u�t")
GetName()
print("~~~~~~~~~~~~�Ҧ����~~~~~~~~~~~~")
NameShow()

import collections

User=collections.namedtuple("User","Name FirstName LastName NameID Part")

data="張:皓博:02360706:資工系"
data=data.split(":")

result=(User(data[0]+data[1], data[0], data[1], data[2], data[3]))

print("姓名:{0} 姓:{1} 名:{2} 編號:{3} 部門:{4} "
          .format(result.Name, result.FirstName, result.LastName
                  , result.NameID, result.Part)) 

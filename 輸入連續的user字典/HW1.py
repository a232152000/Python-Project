import collections

User=collections.namedtuple("User","Name FirstName LastName NameID Part")

data="�i:�q��:02360706:��u�t"
data=data.split(":")

result=(User(data[0]+data[1], data[0], data[1], data[2], data[3]))

print("�m�W:{0} �m:{1} �W:{2} �s��:{3} ����:{4} "
          .format(result.Name, result.FirstName, result.LastName
                  , result.NameID, result.Part)) 

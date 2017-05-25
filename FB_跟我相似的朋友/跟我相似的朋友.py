import facebook # pip install facebook-sdk
import json
import math
from prettytable import PrettyTable
from collections import Counter
from operator  import itemgetter
from matplotlib import pyplot as plt
from numpy import arange

# A helper function to pretty-print Python objects as JSON

def pp(o): 
    print (json.dumps(o, indent=1))

# Create a connection to the Graph API with your access token
ACCESS_TOKEN= 'EAACEdEose0cBAFtdrZAeCEPGtvo4TKn2G5wtR7xCdCa65fh1W2G7RNzyDunEaBZCpYwJqVa01re6A7RzeYPs3ZApau3JaiEh6uiNlQZC7etouDlZAItDDaBpovLpQ66TbfSSllZAuoXqz7Pcvhxi6sfGQX5kEEsLeOmOgCLgezf1XUdoeZB1p5YSpShOfXpzGcZD'

g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }

friends_likes = Counter([like['name']
                         for friend in likes 
                           for like in likes[friend]
                               if like.get('name')])

# Which of your likes are in common with which friends?
my_likes = [ like['name'] 
             for like in g.get_connections("me", "likes")['data'] ]

pt = PrettyTable(field_names=["Name"])
pt.align = 'l'
[ pt.add_row((ml,)) for ml in my_likes ]
print ("My likes")
print (pt)

# Use the set intersection as represented by the ampersand
# operator to find common likes.

common_likes = list(set(my_likes) & set(friends_likes))

# Which of your friends like things that you like?

similar_friends = [ (friend, friend_like['name']) 
                     for friend, friend_likes in likes.items()
                       for friend_like in friend_likes
                         if friend_like.get('name') in common_likes ]


# Filter out any possible duplicates that could occur

ranked_friends = Counter([ friend for (friend, like) in list(set(similar_friends)) ])


pt = PrettyTable(field_names=["Friend", "Number of Common Likes"])
pt.align["Friend"], pt.align["Common Likes"] = '1', 'r'
[ pt.add_row(rf) 
  for rf in sorted(ranked_friends.items(), 
                   key=itemgetter(1), 
                   reverse=True) ]
print ("My similar friends (ranked),第一種")
print (pt)
###############################################################
ranked_friends = Counter([ friend for (friend, like) in list(set(similar_friends)) ])
for i in Counter([ friend for (friend, like) in list(set(similar_friends)) ]):
    ranked_friends[i]=ranked_friends[i]/len(my_likes)


pt = PrettyTable(field_names=["Friend", "Number of Common Likes"])
pt.align["Friend"], pt.align["Common Likes"] = '1', 'r'
[ pt.add_row(rf) 
  for rf in sorted(ranked_friends.items(), 
                   key=itemgetter(1), 
                   reverse=True) ]
print ("My similar friends (ranked),第二種")
print (pt)
################取得me_list和friends_dict#############################################
 
friends_likes_total = [like['name']
                     for friend in likes 
                       for like in likes[friend]
                           if like.get('name')]

friends_likes=[]
friends_dict={}
for friend in likes:
    friends_likes = [like['name'] 
                       for like in likes[friend]
                           if like.get('name')]
    b=[]
    for i in friends_likes_total:
        for j in friends_likes:
            if (j in i):
                b.append(1)
            else:
                b.append(0)   
    friends_dict[friend]=b
         
# Which of your likes are in common with which friends?
my_likes = [ like['name'] 
         for like in g.get_connections("me", "likes")['data'] ]


me_list=[]
for friend in friends_likes_total:
    for i in my_likes:
        if (i in friend):
            me_list.append(1)
        else:
            me_list.append(0)
        
##############################################################
friends_dict_count={}

for friend in likes:
    x=[]
    count=0
    x=friends_dict.get(friend)
    for i in range(len(friends_dict[friend])):
        if(x[i] or me_list[i]):
            count+=1
    friends_dict_count[friend]=count

for i in Counter([ friend for (friend, like) in list(set(similar_friends)) ]):
    ranked_friends[i]=ranked_friends[i]/friends_dict_count[i]


pt = PrettyTable(field_names=["Friend", "Number of Common Likes"])
pt.align["Friend"], pt.align["Common Likes"] = '1', 'r'
[ pt.add_row(rf) 
  for rf in sorted(ranked_friends.items(), 
                   key=itemgetter(1), 
                   reverse=True) ]
print ("My similar friends (ranked),第三種")
print (pt)
#################################################################

    
friends_dict_count = {}
for friend in likes:
    x=[]
    x=friends_dict.get(friend)
    friends_dict_count[friend]=x.count(1)



ranked_friends = Counter([ friend for (friend, like) in list(set(similar_friends)) ])
for i in Counter([ friend for (friend, like) in list(set(similar_friends)) ]):
    ranked_friends[i]=ranked_friends[i]/math.sqrt(me_list.count(1)) * math.sqrt(friends_dict_count[i])


pt = PrettyTable(field_names=["Friend", "Number of Common Likes"])
pt.align["Friend"], pt.align["Common Likes"] = '1', 'r'
[ pt.add_row(rf) 
  for rf in sorted(ranked_friends.items(), 
                   key=itemgetter(1), 
                   reverse=True) ]
print ("My similar friends (ranked),第四種")
print (pt)


    


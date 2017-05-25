import twitter
import json
import sys
import collections
import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph

#------
def tw_oauth(authfile):
    with open(authfile, "r") as f:
        ak = f.readlines() #read the keys and secrets
    f.close()
    CONSUMER_KEY = ak[0].replace("\n","")
    CONSUMER_SECRET = ak[1].replace("\n","")
    OAUTH_TOKEN = ak[2].replace("\n","")
    OAUTH_TOKEN_SECRET = ak[3].replace("\n","")
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)
def getFollowerList(userName):
    followers = []
    cursor = -1  #start page
    while cursor != 0:
        response = twitter_api.followers.list(screen_name=userName, cursor=cursor)
        if response is not None:
            followers += response['users']
            cursor = response['next_cursor']
        if len(followers) > 100 or response is None:
            break
    return followers
def getFriendList(userName):
    friends = []
    cursor = -1  #start page
    while cursor != 0:
        response = twitter_api.friends.list(screen_name=userName, cursor=cursor)
        if response is not None:
            friends += response['users']
            cursor = response['next_cursor']
        if len(friends) > 100 or response is None:
            break
    return friends
def getGroupShip(followerList, friendList):
    follower_name = []
    friend_name = []
    #抓出追隨者名稱
    for user in followerList:
        follower_name.append(user['name'])
    #抓出朋友名稱
    for user in friendList:
        friend_name.append(user['name'])
    #加成一組
    group_follower_name.append(follower_name)
    group_friend_name.append(friend_name)
def saveJson(followList, friendList, groupMemberList):
    #第一個人追隨的,第一個人被追的,第一個人,...
    print ('force.json file save...')
    nxg = nx.DiGraph() #not nx.Graph
    loopCount = 0
    for name in groupMemberList:
        [ nxg.add_edge( mf, name, {'type': 'licensing'}) for mf in followList[loopCount] ]

        [ nxg.add_edge( name, mf,{'type': 'suit'}) for mf in friendList[loopCount] ]
        print(str(loopCount))
        loopCount+=1

    # Start from here to save to json file
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('force.json','w'))
    print ('Save Done!')
#------
group_member_id= ["le8419951779", "a232152000"]
group_member_name = ["樂仲珉", "張皓博"]
group_follower_name = []
group_friend_name = []

twitter_api = tw_oauth("auth.txt") 
print (twitter_api)

for member_id in group_member_id:
    followerList = getFollowerList(member_id)
    friendList = getFriendList(member_id)
    print(str(member_id) + " You have " + str(len(followerList)) + " followers")
    print(str(member_id) + " You have " + str(len(friendList)) + " friends")
    getGroupShip(followerList, friendList)

#畫畫畫
saveJson(group_follower_name, group_friend_name, group_member_name)

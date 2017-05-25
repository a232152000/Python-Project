# -*- coding: utf-8 -*-
import twitter
import json
import sys

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

twitter_api = tw_oauth("auth.txt") 
print (twitter_api)
###############################################
def FollersFriends(name):
    user_name = name
    followers = []
    cursor = -1  #start page
    while cursor != 0:
        response = twitter_api.followers.ids(screen_name=user_name, cursor=cursor)
        if response is not None:
            followers += response['ids']
            cursor = response['next_cursor']
        if len(followers) > 100 or response is None:
            break
    friends = twitter_api.friends.ids(screen_name=user_name, count=100)
    return  followers,friends

def SetPeople(followers,friends):
    get = set(followers) | set(friends['ids'])
    return get

def PeopleDict(user_name,setpeople,user_name_2,setpeople_2):
    friend_dict = {}
    friend_dict_2 = {}
    
    for i in setpeople:
        f = twitter_api.users.lookup(user_id=i)
        print(user_name + " --> " + str(i))
        friend_dict[i] =f[0]["name"]

    for i in setpeople_2:
        f = twitter_api.users.lookup(user_id=i)
        print(user_name_2 + " --> " + str(i))
        friend_dict_2[i] =f[0]["name"]

    friend_dict = {user_name: friend_dict , user_name_2: friend_dict_2}
    return friend_dict

user_name= "a232152000"
followers,friends = FollersFriends(user_name)
setpeople = SetPeople(followers,friends)

user_name_2= "le8419951779"
followers_2,friends_2 = FollersFriends(user_name_2)
setpeople_2 = SetPeople(followers_2,friends_2)

friend_dict = PeopleDict(user_name,setpeople,user_name_2,setpeople_2)
#print(friend_dict)
print("---------------------JSON---------------------")
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print(str(friend_dict).translate(non_bmp_map))

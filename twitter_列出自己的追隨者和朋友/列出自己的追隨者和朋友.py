# -*- coding: utf-8 -*-
import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

						   
# AUTHENTICATION (OAuth)
# It needs an auth file in the following format:
# Your CONSUMER_KEY 
# Your CONSUMER_SECRET 
# Your OAUTH_TOKEN 
# Your OAUTH_TOKEN_SECRET 

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
	


twitter_api = tw_oauth("auth.txt") #Get an twitter_api object

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print (twitter_api)

###############################################
#Get followers and friends(whom you followed)
#This is a simpler version
#response = twitter_api.followers.ids(screen_name=user_name, count=100) #call first time
user_name= "a232152000"
followers = []
cursor = -1  #start page
while cursor != 0:
    response = twitter_api.followers.ids(screen_name=user_name, cursor=cursor)
    if response is not None:
        followers += response['ids']
        cursor = response['next_cursor']
    if len(followers) > 100 or response is None:
        break

    
for id in followers:
    f = twitter_api.users.lookup(user_id=id)
    if(f[0]["name"]!="樂仲珉"):
        print (f[0]["name"])
    
friends = twitter_api.friends.ids(screen_name=user_name, count=100)
for id in friends['ids']:
    f = twitter_api.users.lookup(user_id=id)
    if(f[0]["name"]!="樂仲珉"):
        print (f[0]["name"])

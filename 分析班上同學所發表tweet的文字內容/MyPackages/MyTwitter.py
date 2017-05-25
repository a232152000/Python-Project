# -*- coding: utf-8 -*-
import twitter
import json
from collections import Counter
import jieba
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download("stopwords")

porter = PorterStemmer()


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
	


#twitter_api = tw_oauth("auth.txt") #Get an twitter_api object

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

#print (twitter_api)

######################################
# Search a given user screenname
######################################
def search_user_tweet(twitter_api, user):
    statuses = twitter_api.statuses.user_timeline(screen_name = user)
    return statuses

######################################

######################################
# Search a given user screenname
######################################
def search_user_tweet_id(twitter_api, user):
    statuses = twitter_api.statuses.user_timeline(user_id = user)
    return statuses

######################################

# Search a given topic
######################################
def search_tweet(twitter_api, topic, count=100, iter=5):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=topic, count=count)
    statuses = search_results['statuses']
    # Iterate through iter more batches of results by following the cursor
    for _ in range(iter):
        #print ("Length of statuses", len(statuses))
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e: # No more results when next_results doesn't exist
            break            
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
        try:
            search_results = twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']
        except ValueError as e2:
            break
    return statuses

###############################   
#collect the tweets text
###############################
def get_tweets_texts(statuses):
    status_texts = [ status['text'] 
                     for status in statuses ] 
    return status_texts

##################################################
# Compute a collection of all words from all tweets
# in Englisg
##################################################
def get_tweets_textwords_en(status_texts):
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '://', '@', '+', 'http' , 'https', '。','#','…','’' , '-', '=']) # remove it if you need punctuation 
   
    words = [ porter.stem(w.lower()).replace(U'\U0001f602', ':D')  for txt in status_texts
              for w in wordpunct_tokenize(txt) if w.lower() not in stop_words]
    return words

##################################################
# Compute a collection of all words from all tweets
# in Traditional Chinese
##################################################
def get_tweets_textwords_tw(status_texts):
    jieba.set_dictionary('dict.txt.big')

    words=[]
    for content in status_texts:
        words += jieba.cut(content, cut_all=False)
    return words

##################################################
# Compute a collection of all words from all tweets
# in Simplified Chinese
##################################################
def get_tweets_textwords_cn(status_texts):
    jieba.set_dictionary('dict.txt')
    words=[]
    for content in status_texts:
        words += jieba.cut(content, cut_all=False)
    return words

################################################
#collect the user names mentioned in the tweets
################################################
def get_tweets_mentioned_names(statuses):
    screen_names = [ user_mention['screen_name'] 
                     for status in statuses
                         for user_mention in status['entities']['user_mentions'] ]
    return screen_names

##########################################
#collect the categories of the tweets
##########################################
def get_tweets_hashtags(statuses):
    hashtags = [ hashtag['text'] 
                 for status in statuses
                     for hashtag in status['entities']['hashtags'] ]
    return hashtags

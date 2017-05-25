from MyPackages import *
from collections import Counter
import operator
import json
import sys
from collections import Counter
from prettytable import PrettyTable
from matplotlib import pyplot 
from prettytable import PrettyTable  


twitter_api = MyTwitter.tw_oauth("auth.txt") #Get an twitter_api object

user = "833911159203827712"

#########讀user_id檔######
fin = open("user_id.txt", encoding="utf8")
content = fin.readlines()
fin.close()

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
timelines=[]
for i in content:
        timelines += MyTwitter.search_user_tweet_id(twitter_api, i)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
for status in timelines:
        print ("{0} {1} ".format(status["created_at"], status["text"].encode("ascii", "ignore")))

texts = MyTwitter.get_tweets_texts(timelines)
words = MyTwitter.get_tweets_textwords_en(texts)
words = MyTwitter.get_tweets_textwords_tw(words)

freq = Counter(words)

print("總篇數:" + str(len(texts)) )
print("平均長度:" + str(len(words)/len(texts)) )

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True) #sorted by counts

freq_dict = [ {"text": w, "size":c*10} for (w, c) in sorted_freq ]
with open('wordcounts.json', 'w') as fp:
        json.dump(freq_dict, fp)

        
###畫   字彙統計：單字，次數。以表格呈現######
print ( "字彙統計：單字，次數。以表格呈現。:") # top 100

x = PrettyTable(["詞彙","頻率"])  
x.align["詞彙"] = "l"# Left align city names
x.padding_width = 1# One space between column edges and contents (default)

a=list(freq.keys())
b=list(freq.values())
for i in range(len(a)):
        x.add_row([a[i],b[i]])  
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print(str(x).translate(non_bmp_map))

############################################
pyplot.plot(b)
pyplot.xticks(range(len(freq)), freq.keys())
pyplot.title("frequency")
pyplot.ylabel("count")
pyplot.xlabel("vocabulary")
pyplot.show()

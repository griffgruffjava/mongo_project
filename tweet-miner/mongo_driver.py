__author__ = 'Ciaran Griffin t00175569'

import pymongo
from pymongo import MongoClient
import re
from collections import Counter
import operator



def add_to_list(tag):
    tag = tag.lower()
    hashtags.append(tag)

client = MongoClient()

db = client.eve

print db

collection = db.cooltweets

print " count is " + (str)(collection.count())

tweets_iterator = collection.find()



found_tags = []

for tweet in tweets_iterator:
    ents = tweet['entities']
    hashtags = []
    hashtags = ents['hashtags']
    for tag in hashtags:
        found_tags.append(str(tag['text']))
        # print "here is a hashtag " + tag['text']

print found_tags

# for tweet in tweets_iterator:
#     tweet_text = tweet['text']
# # #     print tweet['text']
#     tags = re.findall(r"#(\w+)", tweet_text)
#     for tag in tags:
#         add_to_list(str(tag))
#
counted = {}
[counted.__setitem__(item, 1+counted.get(item, 0)) for item in found_tags]
#
sorted_counted = sorted(counted.items(), key=operator.itemgetter(1)) #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value


print sorted_counted
for item in sorted_counted:
    print item
# # for key, value in sorted_counted.items():
# #     print (key, value)
#
#
#
#
print len(counted)
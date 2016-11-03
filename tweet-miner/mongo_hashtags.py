__author__ = 'Ciaran Griffin t00175569'

from pymongo import MongoClient
import operator

client = MongoClient()

db = client.eve

collection = db.cooltweets

tweets_iterator = collection.find()

found_tags = []

for tweet in tweets_iterator:
    entities = tweet['entities']
    hashtags = entities['hashtags']
    for tag in hashtags:
        try:
            found_tags.append(str(tag['text']))
        except UnicodeEncodeError:
            print "malformed tag encoding - " + tag['text']

counted = {}

# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
[counted.__setitem__(item, 1+counted.get(item, 0)) for item in found_tags]
sorted_counted = sorted(counted.items(), key=operator.itemgetter(1))

print sorted_counted
for item in sorted_counted:
    print item

print "Total number of tweets collected is " + str(collection.count())
print "The number of unique Hashtags is " + str(len(counted))

from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId

client = MongoClient('localhost:27017')

db = client['eve']
tweets = db['tweets']

# CREATE methods - single and multi


def create_tweet(tweet):
    tweet = tweets.insert_one(tweet)
    return tweet


def multi_create_tweet(multi_tweet):
    created_tweets = tweets.insert_many(multi_tweet)
    return created_tweets

#  READ methods


def get_tweet_by_id(id):
    print tweets.count()
    return tweets.find_one({'_id': ObjectId(id)})



def get_first_tweet(key, value):
        found_tweet = tweets.find_one({key: value})
        return found_tweet


def get_all():
    return tweets.find()


# Update methods


def update_tweet(id, key, value):
    return tweets.find_one_and_update({'_id': ObjectId(id)}, {'$set': {key: value}}, return_document=ReturnDocument.AFTER)



data1 = {'name': 'Mongo_God', 'text': 'On the 8th day I made a tweet'}
data2 = [data1, {'name': 'Mongo_God', 'text': 'more tweeting here'}]

# print create_tweet(data1)

# print multi_create_tweet(data2)

# print get_tweet_by_id("581bc6610bdb82869e9ed989")

# print get_first_tweet('name','Mongo_God')

# print get_all()


print update_tweet("581bc6610bdb82869e9ed989", 'text', 'i am so awesome!')

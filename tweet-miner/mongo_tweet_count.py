__author__ = 'Ciaran Griffin t00175569'

from pymongo import MongoClient

client = MongoClient()

db = client.eve

collection = db.cooltweets

tweets_iterator = collection.find()

print "Total number of tweets collected is " + str(collection.count())

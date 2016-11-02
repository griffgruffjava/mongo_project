__author__ = 'Ciaran Griffin t00175569'
"""
Author: Ruben
Cuevas
Menendez
Download and store
tweets in MongoDB.
"""

import json

import tweepy
from pymongo import MongoClient


class StreamListener(tweepy.StreamListener):
    # tweepy.StreamListener is a class provided by tweepy used to access the Twitter Streaming API. It allows us to retrieve tweets in real time.

    def on_connect(self):
        print("You're connected to the streaming server.")

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

    def on_data(self, data):
        client = MongoClient('localhost', 27017)

        # Use cooldb database
        db = client.eve

        # Decode JSON
        datajson = json.loads(data)
        # text = datajson["text"]
        #
        # # print text
        # word = "trump"
        # if word in text.lower():
        #     datajson ['trump_mention'] = 1
        # word = "clinton"
        # if word in text.lower:
        #     datajson ['clinton_mention'] = 1

        # We only want to store tweets in English
        if "lang" in datajson and datajson["lang"] == "en":
            # Store tweet info into the cooltweets collection.
            db.cooltweets.insert(datajson)


# This is a manually created filed where I stored my OAuth credentials for Twitter.
# Each line is a key-value pair of the form: KEY_NAME:KEY
# CREDENTIALS_PATH = 'C:/Users/Finbar/Desktop/twitter_keys/keys.txt'
# CREDENTIALS_PATH = 'C:/Users/t00175569/Desktop/twitter_keys/keys.txt'
CREDENTIALS_PATH = '/Users/C_Train/Desktop/twitter_keys/keys.txt'
# Path to the list of Spanish stop words.
# STOPWORDS_ES_PATH = 'C:/Users/Finbar/Desktop/twitter_keys/keywords.txt'
# STOPWORDS_ES_PATH = 'C:/Users/t00175569/Desktop/twitter_keys/keywords.txt'
STOPWORDS_ES_PATH = '/Users/C_Train/Desktop/twitter_keys/keywords.txt'

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Load credentials

with open(CREDENTIALS_PATH) as f:
    for line in f:
        line = line.rstrip('\r\n').split(":")
        if line[0] == "CONSUMER_KEY":
            CONSUMER_KEY = line[1]
        elif line[0] == "CONSUMER_SECRET":
            CONSUMER_SECRET = line[1]
        elif line[0] == "ACCESS_TOKEN":
            ACCESS_TOKEN = line[1]
        elif line[0] == "ACCESS_TOKEN_SECRET":
            ACCESS_TOKEN_SECRET = line[1]

# Authenticating
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

l = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth1, listener=l)
with open(STOPWORDS_ES_PATH) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])

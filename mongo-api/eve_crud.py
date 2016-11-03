import requests

import json_utils

base = 'http://127.0.0.1:5000/cooltweets'


# CREATE CALLS - HTTP POST

def post_tweet(insert_json):
    req = requests.post(base, insert_json)
    return req


# READ CALLS - HTTP GET

def get_all_by_pagination(page_size, page):
    if page_size > 50:
        print "max page size is 50, results will reflect this."
    req = requests.request('GET', base + "?max_results=" + str(page_size) + "&page=" + str(page))
    return req.text


def get_by_mongo_id(mongo_id):
    req = requests.request('GET', base + "/" + mongo_id)
    return req.text


def get_by_tweet_id(tweet_id):
    req = requests.request('GET', base + '?where={"id":' + str(tweet_id) + '}')
    return req.text


def get_tweet_by_field(field, value):
    if isinstance(value, basestring):
        req = requests.request('GET', base + '?where={"' + field + '":"' + value + '"}')
        return req.text
    else:
        req = requests.request('GET', base + '?where={"' + field + '":' + str(value) + '}')
        return req.text


# UPDATE CALLS - HTTP PUT, PATCH


def put_tweet(mongo_id, replacement):
    reg_text = get_by_mongo_id(mongo_id)
    json_tweet = json_utils.json_loads_byteified(reg_text)
    etag = json_tweet["_etag"]
    headers = {'If-Match': etag}
    reg = requests.put(base + "/" + str(mongo_id), replacement, headers=headers)
    return reg


def patch_tweet_by_field(mongo_id, field, value):
    reg_text = get_by_mongo_id(mongo_id)
    json_tweet = json_utils.json_loads_byteified(reg_text)
    data = {field: value}
    print data
    etag = json_tweet["_etag"]
    headers = {'If-Match': etag}
    reg = requests.patch(base + "/" + str(mongo_id), data, headers=headers)
    return reg


# DELETE CALLS - HTTP DELETE


def delete_collection():
    req = requests.request('DELETE', base)
    return req


def delete_tweet(mongo_id):
    reg_text = get_by_mongo_id(mongo_id)
    json_tweet = json_utils.json_loads_byteified(reg_text)
    etag = json_tweet["_etag"]
    headers = {'If-Match': etag}
    req = requests.request('DELETE', base + '/' + str(mongo_id), headers=headers)
    return req


# print get_by_mongo_id("581b2f2beec9cc11803a6d59")

# print get_by_tweet_id(794156147741786112)

# print get_tweet_by_field("id", 794156147741786112)

# print get_tweet_by_field("user.screen_name", "10_After")

# print get_tweet_by_field("user.wrong_field", "10_After")

# print get_all_by_pagination(1000, 3)

# print get_all_by_pagination(35, 3)

# data = {'text': 'IS THIS STILL THING ON??'}
# put_tweet("581b2f2beec9cc11803a6d59", data)

# patch_tweet_by_field("581b2f2beec9cc11803a6d59", "text", "same_value again!!")
# print get_by_mongo_id("581b2f2beec9cc11803a6d59")

# patch_tweet_by_field("581b2f2beec9cc11803a6d59", "wrong_field_name", "same_value")
# print get_by_mongo_id("581b2f2beec9cc11803a6d59")

# data = {'screen_name': "da_bad_ass", 'text': "this is a tweet mofo"}
# print post_tweet(data)


delete_collection()

# print delete_tweet("581b2f2beec9cc11803a6d59")

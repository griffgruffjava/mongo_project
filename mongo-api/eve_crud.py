import requests
import json


# Json helper methods
# http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )


def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )


def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

base = 'http://127.0.0.1:5000/cooltweets'

# CREATE CALLS - HTTP POST

def post_tweet( insert_json ):
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


def put_tweet_by_field( mongo_id, replacement):
    reg_text = get_by_mongo_id(mongo_id)
    json_tweet = json_loads_byteified(reg_text)
    etag = json_tweet["_etag"]
    headers = {'If-Match': etag}
    reg = requests.put(base + "/" + str(mongo_id), replacement, headers=headers)
    return reg


def patch_tweet_by_field( mongo_id, field, value):
    reg_text = get_by_mongo_id(mongo_id)
    json_tweet = json_loads_byteified(reg_text)
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
    json_tweet = json_loads_byteified(reg_text)
    etag = json_tweet["_etag"]
    headers = {'If-Match': etag}
    req = requests.request('DELETE', base + '/' + str(mongo_id), headers=headers)
    return req

# print get_by_mongo_id("5819f928eec9cc20742ed3d7")

# print get_by_tweet_id(793823277630255104)

# print get_tweet_by_field("id", 793823277630255104)

# print get_tweet_by_field("user.screen_name", "NorthmetroCnx")

# print get_tweet_by_field("user.wrong_field", "NorthmetroCnx")

# print get_all_by_pagination(1000, 3)

# print get_all_by_pagination(35, 3)
# data = {'text': 'IS THIS THING ON??'}
# put_tweet_by_field("5819f928eec9cc20742ed3d7", data)
# patch_tweet_by_field("5819f928eec9cc20742ed3d7", "text", "same_value")
# print get_by_mongo_id("5819f928eec9cc20742ed3d7")

# data = {'screen_name': "da_bad_ass", 'text': "this is a tweet mofo"}
# print post_tweet(data)


delete_collection()

# print delete_tweet("581b2981eec9cc1f80a155b9")


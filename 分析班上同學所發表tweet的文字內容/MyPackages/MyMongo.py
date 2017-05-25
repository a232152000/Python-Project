import json
import pymongo #pip install pymongo

def save_mongo(data, db_name, collection_name, **mongo_conn_kw):
    client = pymongo.MongoClient(**mongo_conn_kw)
    db = client[db_name]
    collection = db[collection_name]
    return collection.insert(data)

def load_mongo(db_name, collection_name, return_cursor=False, criteria=None, projection=None, **mongo_conn_kw):
    client = pymongo.MongoClient(**mongo_conn_kw)
    db = client[db_name]
    collection = db[collection_name]
    if criteria is None:
        criteria = {}
    if projection is None:
        cursor= collection.find(criteria)
    else:
        cursor= collection.find(criteria, projection)

    if return_cursor:
        return cursor
    else:
        return [item for item in cursor]
    
#Sample usage
    
#twitter_api = tw_oauth("auth.txt") #Get an twitter_api object
#user_id = '438081730'
#statuses = twitter_api.users.lookup(user_id=user_id)

#save_mongo(statuses, "test", "profile")
#profile = load_mongo("test", "profile")

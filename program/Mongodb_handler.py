from pymongo import MongoClient


def connect_to_mongodb(db_url, db_name):
    client = MongoClient(db_url)
    db = client[db_name]
    return db

def save_notes(db, collection_name, xml_data,name):
    message = {name:xml_data}
    collection = db[collection_name]
    collection.insert_one(message)


def save_users(db, collection_name, name, password):
    message = {name: password}
    collection = db[collection_name]
    collection.insert_one(message)

def find_notes(db, collection_name, name):
    collection = db[collection_name]
    document = list(collection.find({},{name:1}))
    for dic in document:
        print(dic)
    




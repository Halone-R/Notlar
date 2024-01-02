from pymongo import MongoClient
from Client import *
from Encrypt import *
uri = "mongodb+srv://saranogueira1:password1990@cluster0.36qrg1i.mongodb.net/?retryWrites=true&w=majority" #change when connecting to a different database
client = MongoClient(uri)

#connect to database
def run():
    try:
        # Connect the client to the server
        client.start_session()
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    finally:
        # Ensures that the client will close when you finish/error
        client.close()


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
    document = list(collection.find({},{'_id':0, name:1}))
    for dic in document:
        print(dic)
    


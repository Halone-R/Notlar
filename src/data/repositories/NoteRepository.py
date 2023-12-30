from src.data.db.DatabaseConnection import BDConnectionHandler
from typing import Dict
from bson.objectid import ObjectId

class UserRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "Notes"
        self.__db_connection = db_connection


    def insert_note(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def delete_note(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.remove_one(document)
        return document

    
    def select_note(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, { "_id": 0})
        return response
    
    def select_by_id(self, _id) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({ "_id": ObjectId(_id)})
        for elem in response: print(elem)
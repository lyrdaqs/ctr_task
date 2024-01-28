from pymongo import MongoClient, DESCENDING
import settings


class MongoConnection:
    def __init__(self, db_name, col_name):
        client = MongoClient(settings.MONGODB_URL)
        self.db = client[db_name][col_name]
        
    def get_documents_by_ids(self, id_list):
        query = {'_id': {'$in': id_list}}
        result = list(self.db.find(query))
        return result
    
    def export(self):
        return self.db.find()
    
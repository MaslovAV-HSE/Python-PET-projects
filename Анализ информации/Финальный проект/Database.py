import pymongo

class mongo():
    def __init__(self, host='localhost', port=27017, db='Bot_Database', col='Users'):
        self.db_client = pymongo.MongoClient(host=host, port=port)
        self.current_db = self.db_client[db]
        self.collection = self.current_db[col]

    def user_exist(self, tid):
        return True if self.collection.find_one({'id': tid}) is not None else False

    def insert_user(self, tid, location=("Null", 0, 0), current_state=0, subscribe=False):
        document = {
            'id': tid,
            'location': location,
            'utf': 0,
            'current_state': current_state,
            'subscribe': subscribe
        }
        self.collection.insert_one(document)

    def change_state(self, tid, state):
        self.collection.update_one({'id': tid}, {"$set": {"current_state": state}})

    def get_state(self, tid):
        return self.collection.find_one({'id': tid})['current_state']

    def change_location(self, tid, location, utf):
        self.collection.update_one({'id': tid}, {"$set": {"location": location, 'utf': utf}})

    def get_location(self, tid):
        return self.collection.find_one({'id': tid})['location']

    def change_subscribe(self, tid, sub):
        self.collection.update_one({'id': tid}, {"$set": {"subscribe": sub}})

    def get_subscribe(self, tid):
        return self.collection.find_one({'id': tid})['subscribe']

    def generate_subscribers_list(self):
        users = self.collection.find()
        return [i for i in users if i['subscribe'] == True]


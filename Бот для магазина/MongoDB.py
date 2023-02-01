import pymongo

'''db_client = pymongo.MongoClient('localhost', 27017)
current_db = db_client["DymovoohaDB"]
collection = current_db["Users"]'''

class mongo():
    def __init__(self, host='localhost', port=27017, db='DymovoohaDB', col='Users'):
        self.db_client = pymongo.MongoClient(host, port)
        self.current_db = self.db_client[db]
        self.collection = self.current_db[col]

    def get_points(self, phone):
        return self.collection.find_one({'phone': phone})['current_points']

    def user_exist(self, phone):
        var = True if self.collection.find_one({'phone': phone}) != None else False
        return var

    def insert_user(self, name, s_name, phone, current_points=500.0, used_points=0.0, purchases=0, sale=2):
        if self.user_exist(phone):return False
        document = {
            'name': name,
            's_name': s_name,
            'phone': phone,
            'current_points': current_points,
            'used_points': used_points,
            'purchases': purchases,
            'sale': sale
        }
        self.collection.insert_one(document)
        return True

    def add_purchase(self, phone, price):
        try:
            if self.user_exist(phone):
                user = self.collection.find_one({'phone': phone})
                purchases = user['purchases']
                curr = user['current_points']
                sale = user['sale']
                if purchases == 0:
                    purchases = [price]
                else:
                    purchases.append(price)
                curr = round(curr + price * (sale / 10), 2)
                self.collection.update_one({'phone': phone}, {"$set": {"purchases": purchases, "current_points": curr}})
                return True
            else:
                return False
        except:
            return False

    def use_points(self, phone, points, purchase):
        try:
            if self.user_exist(phone):
                user = self.collection.find_one({'phone': phone})
                if user['current_points'] >= points and purchase * 0.45 >= points / 10 and len(user['purchases']) >= 2:
                    curr = round(user['current_points'] - points, 2)
                    used = round(user['used_points'] + points, 2)
                    self.collection.update_one({'phone': phone}, {"$set": {"used_points": used, 'current_points': curr}})
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def user_sale(self, phone, sale, sett=False):
        try:
            if self.user_exist(phone):
                user = self.collection.find_one({'phone': phone})
                if not sett:
                    self.collection.update_one({'phone': phone}, {"$set": {"sale": sale}})
                else:
                    return user['sale']
            else:
                return False
        except:
            return False
    def data_to_excel(self):
        data = list(self.collection.find())


test = mongo()
test.data_to_excel()




'''def get_connection(host='localhost', port=27017, db='DymovoohaDB', col='Users'):
    global db_client, current_db, collection
    db_client = pymongo.MongoClient(host, port)
    current_db = db_client[db]
    collection = current_db[col]


def user_exist(phone):
    var = True if collection.find_one({'phone': phone}) != None else False
    return var

def insert_user(name, s_name, phone, current_points=500.0, used_points=0.0, purchases=0, sale=2):
    global collection
    document = {
        'name': name,
        's_name': s_name,
        'phone': phone,
        'current_points': current_points,
        'used_points': used_points,
        'purchases': purchases,
        'sale': sale
    }
    collection.insert_one(document)

def add_purchase(phone, price):
    try:
        if user_exist(phone):
            user = collection.find_one({'phone': phone})
            purchases = user['purchases']
            curr = user['current_points']
            sale = user['sale']
            if purchases == 0:
                purchases = [price]
            else:
                purchases.append(price)
            curr = curr + price * (sale / 10)
            collection.update_one({'phone': phone}, {"$set": {"purchases": purchases, "current_points": curr}})
            return True
        else:
            return False
    except:
        return False


def use_points(phone, points, purchase):
    try:
        if user_exist(phone):
            user = collection.find_one({'phone': phone})
            if user['current_points'] > points and purchase * 0.45 >= points / 10:
                curr = user['current_points'] - points
                used = user['used_points'] + points
                collection.update_one({'phone': phone}, {"$set": {"used_points": used, 'current_points': curr}})
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def user_sale(phone, sale, set = False):
    try:
        if user_exist(phone):
            user = collection.find_one({'phone': phone})
            if not set:
                collection.update_one({'phone': phone}, {"$set": {"sale": sale}})
            else:
                return user['sale']
        else:
            return False
    except:
        return False
'''


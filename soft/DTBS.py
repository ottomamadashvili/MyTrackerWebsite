from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://admin:12341234@cluster0.1ddpj.mongodb.net/MyMa_db?retryWrites=true&w=majority")
db = cluster["MyMa_db"]
collections = db["main"]
restricted_ones=[]
restricted_array= collections.find_one({"_id": '33003300'}) #Restricted array in my database has this ID, change with yours




def ID_exists(idValue):
    if collections.count_documents(idValue) == 0:
        return True

def posting_data(first_dict):
    collections.insert_one(first_dict)


def update_data(somedict, idValue):
    collections.update_one({"_id" : idValue}, {"$set" : somedict})


def restricted_accounts(userID_value):
    if userID_value not in restricted_array:
        return True


#adding values into restricted array: example:
#collections.update_one({"_id": '33003300'}, {"$push": {'restricted_ones': 2256575}})

#clear database.
# collections.delete_many({"_id":{"$nin":["33003300"]}})
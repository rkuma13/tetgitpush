import pymongo


client = pymongo.MongoClient("mongodb+srv://root:root@rajancluster0.ub5nt.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)



d = {
    "name":"Rajan111",
    "email": "rajansharmassi@gmail.com",
    "surname": "Kumar"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)